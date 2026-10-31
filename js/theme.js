(() => {
  const storageKey = "recon-osint-theme";
  const fontStorageKey = "recon-osint-font-scale";
  const minFontScale = 0.8;
  const maxFontScale = 1.2;
  const fontStep = 0.05;
  const root = document.documentElement;
  let speaker = null;
  let channel = null;

  function syncSpeaker(theme) {
    if (!speaker || speaker.closed) return;
    try {
      const doc = speaker.document;
      doc.documentElement.dataset.theme = theme;
      doc.documentElement.dataset.fontScale = root.dataset.fontScale || "1";
      if (!doc.getElementById("presentation-speaker-theme")) {
        const link = doc.createElement("link");
        link.id = "presentation-speaker-theme";
        link.rel = "stylesheet";
        link.href = new URL("css/08-speaker-theme.css", document.baseURI).href;
        doc.head.appendChild(link);
      }
      doc.querySelectorAll("#current-slide iframe, #upcoming-slide iframe").forEach((frame) => {
        const syncFrame = () => {
          try {
            if (frame.contentWindow.PresentationTheme) frame.contentWindow.PresentationTheme.applyRemote(root.dataset.theme || "dark");
          } catch (_) { /* A prévia ainda está carregando. */ }
        };
        if (!frame.dataset.themeSync) {
          frame.dataset.themeSync = "true";
          frame.addEventListener("load", syncFrame);
        }
        syncFrame();
      });
    } catch (_) { /* A janela foi fechada ou deixou de ser acessível. */ }
  }

  function applyRemote(theme) {
    if (theme === "light") root.dataset.theme = "light";
    else delete root.dataset.theme;
    syncSpeaker(theme === "light" ? "light" : "dark");
  }

  function toggle() {
    const theme = root.dataset.theme === "light" ? "dark" : "light";
    applyRemote(theme);
    try { localStorage.setItem(storageKey, theme); } catch (_) { /* Sem persistência. */ }
    if (channel) channel.postMessage(theme);
    // A prévia do Speaker View pode atualizar diretamente a janela original,
    // mesmo quando o armazenamento local e BroadcastChannel estão bloqueados.
    try {
      if (window.parent !== window && window.parent.opener && window.parent.document.querySelector("#speaker-controls")) {
        window.parent.opener.PresentationTheme.applyRemote(theme);
      }
    } catch (_) { /* Outra origem não participa da sincronização. */ }
  }

  function applyFontRemote(scale) {
    const value = Math.min(maxFontScale, Math.max(minFontScale, Number(scale) || 1));
    root.dataset.fontScale = value.toFixed(2);
    root.classList.toggle("font-scale-large", value >= 1.1);
    root.style.setProperty("--presentation-font-scale", value.toFixed(2));
    syncFontSpeaker(value.toFixed(2));
  }

  function syncFontSpeaker(scale) {
    if (!speaker || speaker.closed) return;
    try {
      const doc = speaker.document;
      doc.documentElement.dataset.fontScale = scale;
      doc.documentElement.style.setProperty("--presentation-font-scale", scale);
      doc.querySelectorAll("#current-slide iframe, #upcoming-slide iframe").forEach((frame) => {
        const syncFrame = () => {
          try { frame.contentWindow.PresentationTheme?.applyFontRemote(scale); } catch (_) { /* A prévia ainda carrega. */ }
        };
        if (!frame.dataset.fontSync) {
          frame.dataset.fontSync = "true";
          frame.addEventListener("load", syncFrame);
        }
        syncFrame();
      });
    } catch (_) { /* A janela foi fechada ou deixou de ser acessível. */ }
  }

  function changeFont(delta) {
    const current = Number(root.dataset.fontScale) || 1;
    const next = Math.min(maxFontScale, Math.max(minFontScale, Math.round((current + delta) * 100) / 100));
    applyFontRemote(next);
    try { localStorage.setItem(fontStorageKey, next.toFixed(2)); } catch (_) { /* Sem persistência. */ }
    if (channel) channel.postMessage({ type: "font-scale", value: next });
    try {
      if (window.parent !== window && window.parent.opener && window.parent.document.querySelector("#speaker-controls")) {
        window.parent.opener.PresentationTheme.applyFontRemote(next);
      }
    } catch (_) { /* Outra origem não participa da sincronização. */ }
  }

  function resetFont() {
    applyFontRemote(1);
    try { localStorage.setItem(fontStorageKey, "1.00"); } catch (_) { /* Sem persistência. */ }
    if (channel) channel.postMessage({ type: "font-scale", value: 1 });
    try {
      if (window.parent !== window && window.parent.opener && window.parent.document.querySelector("#speaker-controls")) {
        window.parent.opener.PresentationTheme.applyFontRemote(1);
      }
    } catch (_) { /* Outra origem não participa da sincronização. */ }
  }

  window.PresentationTheme = {
    toggle,
    applyRemote,
    increaseFont: () => changeFont(fontStep),
    decreaseFont: () => changeFont(-fontStep),
    resetFont,
    applyFontRemote,
  };
  try {
    applyRemote(localStorage.getItem(storageKey));
    applyFontRemote(localStorage.getItem(fontStorageKey));
  } catch (_) { /* Padrão escuro e escala padrão. */ }
  try {
    channel = new BroadcastChannel(storageKey);
    channel.addEventListener("message", (event) => {
      if (event.data === "light" || event.data === "dark") applyRemote(event.data);
      else if (event.data?.type === "font-scale") applyFontRemote(event.data.value);
    });
  } catch (_) { /* O evento de storage e o contato direto são alternativas. */ }
  window.addEventListener("storage", (event) => {
    if (event.key === storageKey) applyRemote(event.newValue);
    if (event.key === fontStorageKey) applyFontRemote(event.newValue);
  });

  // O plugin de notas abre uma janela da mesma origem e anuncia a conexão.
  window.addEventListener("message", (event) => {
    if (event.origin !== window.location.origin || typeof event.data !== "string") return;
    try {
      const data = JSON.parse(event.data);
      if (data.namespace === "reveal-notes" && (data.type === "connected" || data.type === "heartbeat")) {
        speaker = event.source;
        syncSpeaker(root.dataset.theme || "dark");
      }
    } catch (_) { /* Ignora mensagens que não pertencem ao plugin. */ }
  });
})();
