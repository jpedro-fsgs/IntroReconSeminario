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
});
