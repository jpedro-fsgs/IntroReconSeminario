(() => {
  const storageKey = "recon-osint-theme";
  const root = document.documentElement;
  let speaker = null;
  let channel = null;

  function syncSpeaker(theme) {
    if (!speaker || speaker.closed) return;
    try {
      const doc = speaker.document;
      doc.documentElement.dataset.theme = theme;
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

  window.PresentationTheme = { toggle, applyRemote };
  try { applyRemote(localStorage.getItem(storageKey)); } catch (_) { /* Padrão escuro. */ }
  try {
    channel = new BroadcastChannel(storageKey);
    channel.addEventListener("message", (event) => {
      if (event.data === "light" || event.data === "dark") applyRemote(event.data);
    });
  } catch (_) { /* O evento de storage e o contato direto são alternativas. */ }
  window.addEventListener("storage", (event) => {
    if (event.key === storageKey) applyRemote(event.newValue);
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
