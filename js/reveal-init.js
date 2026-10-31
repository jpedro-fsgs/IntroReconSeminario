Reveal.initialize({
  width: 1280,
  height: 720,
  margin: 0,
  minScale: 0.2,
  maxScale: 1.6,

  // Navegação exclusivamente horizontal: não há seções verticais aninhadas.
  center: false,
  controls: true,
  controlsLayout: "bottom-right",
  controlsBackArrows: "faded",
  progress: true,
  slideNumber: "c/t",
  hash: true,
  history: false,

  transition: "slide",
  transitionSpeed: "default",
  backgroundTransition: "fade",

  keyboard: true,
  overview: true,
  touch: true,
  loop: false,

  plugins: [RevealHighlight, RevealNotes, RevealSearch]
}).then(() => {
  Reveal.addKeyBinding({ keyCode: 84, key: "T", description: "Alternar tema claro/escuro" }, () => {
    window.PresentationTheme.toggle();
  });
  Reveal.addKeyBinding({ keyCode: 187, key: "+", description: "Aumentar fonte" }, () => window.PresentationTheme.increaseFont());
  Reveal.addKeyBinding({ keyCode: 107, key: "Num +", description: "Aumentar fonte" }, () => window.PresentationTheme.increaseFont());
  Reveal.addKeyBinding({ keyCode: 189, key: "-", description: "Diminuir fonte" }, () => window.PresentationTheme.decreaseFont());
  Reveal.addKeyBinding({ keyCode: 109, key: "Num -", description: "Diminuir fonte" }, () => window.PresentationTheme.decreaseFont());
  Reveal.addKeyBinding({ keyCode: 48, key: "0", description: "Restaurar tamanho da fonte" }, () => window.PresentationTheme.resetFont());
});
