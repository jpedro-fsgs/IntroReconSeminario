// Teste opcional com Playwright e um servidor local já em execução.
const assert = require("node:assert/strict");
const { chromium } = require("playwright");

const url = process.env.TEST_URL || "http://localhost:8791/_site/";

async function testTheme(browser, withoutStorage) {
  const context = await browser.newContext({ viewport: { width: 1280, height: 720 }, reducedMotion: "reduce" });
  if (withoutStorage) {
    await context.addInitScript(() => {
      Object.defineProperty(window, "localStorage", { get() { throw new Error("blocked"); } });
      window.BroadcastChannel = undefined;
    });
  }
  const page = await context.newPage();
  const errors = [];
  page.on("pageerror", (error) => errors.push(error.message));
  await page.goto(url, { waitUntil: "networkidle" });
  await page.waitForFunction(() => Reveal.isReady());
  await page.keyboard.press("t");
  assert.equal(await page.evaluate(() => document.documentElement.dataset.theme), "light");
  assert.equal(await page.evaluate(() => Reveal.getIndices().h), 0);
  await page.keyboard.press("+");
  assert.equal(await page.evaluate(() => document.documentElement.dataset.fontScale), "1.05");
  for (let step = 0; step < 3; step += 1) await page.keyboard.press("+");
  assert.equal(await page.evaluate(() => document.documentElement.dataset.fontScale), "1.20");
  const clippedSlides = await page.evaluate(async () => {
    await document.fonts.ready;
    const clipped = [];
    for (let index = 0; index < Reveal.getTotalSlides(); index += 1) {
      Reveal.slide(index);
      const overflow = [...Reveal.getCurrentSlide().querySelectorAll("h1,h2,h3,h4,p,li,.chip,.small,.lede,.source,.geo-card,.tool-detail-copy,.tool-detail-result")]
        .map((element) => {
          const box = element.getBoundingClientRect();
          const slide = Reveal.getCurrentSlide().getBoundingClientRect();
          return box.width && (box.top < slide.top - 1 || box.bottom > slide.bottom + 1 || box.left < slide.left - 1 || box.right > slide.right + 1)
            ? element.textContent.trim().slice(0, 50)
            : null;
        }).filter(Boolean);
      if (overflow.length) clipped.push({ slide: index + 1, elements: overflow });
    }
    Reveal.slide(0);
    return clipped;
  });
  assert.deepEqual(clippedSlides, []);
  await page.keyboard.press("+"); // respeita o limite superior
  assert.equal(await page.evaluate(() => document.documentElement.dataset.fontScale), "1.20");
  for (let step = 0; step < 4; step += 1) await page.keyboard.press("-");
  assert.equal(await page.evaluate(() => document.documentElement.dataset.fontScale), "1.00");
  await page.keyboard.press("-");
  assert.equal(await page.evaluate(() => document.documentElement.dataset.fontScale), "0.95");
  for (let step = 0; step < 3; step += 1) await page.keyboard.press("-");
  assert.equal(await page.evaluate(() => document.documentElement.dataset.fontScale), "0.80");
  await page.keyboard.press("-"); // respeita o limite inferior
  assert.equal(await page.evaluate(() => document.documentElement.dataset.fontScale), "0.80");
  await page.keyboard.press("0");
  assert.equal(await page.evaluate(() => document.documentElement.dataset.fontScale), "1.00");

  const [speaker] = await Promise.all([page.waitForEvent("popup"), page.keyboard.press("s")]);
  speaker.on("pageerror", (error) => errors.push(error.message));
  await speaker.waitForFunction(() => document.documentElement.dataset.theme === "light" &&
    document.querySelectorAll("iframe").length === 2 &&
    [...document.querySelectorAll("iframe")].every((frame) => frame.contentWindow.Reveal?.isReady() && frame.contentDocument.documentElement.dataset.theme === "light"));

  await page.keyboard.press("+");
  await speaker.waitForFunction(() => document.documentElement.dataset.fontScale === "1.05" &&
    [...document.querySelectorAll("iframe")].every((frame) => frame.contentDocument.documentElement.dataset.fontScale === "1.05"));
  await speaker.waitForFunction(() => getComputedStyle(document.body).fontSize === "18.9px");
  for (let step = 0; step < 3; step += 1) await page.keyboard.press("+");
  await speaker.waitForFunction(() => document.documentElement.dataset.fontScale === "1.20" &&
    [...document.querySelectorAll("iframe")].every((frame) => frame.contentDocument.documentElement.dataset.fontScale === "1.20"));
  await speaker.waitForFunction(() => getComputedStyle(document.body).fontSize === "21.6px");
  await speaker.keyboard.press("+"); // o teto continua valendo no Speaker View
  assert.equal(await page.evaluate(() => document.documentElement.dataset.fontScale), "1.20");
  await speaker.keyboard.press("0");
  await page.waitForFunction(() => document.documentElement.dataset.fontScale === "1.00");
  await page.keyboard.press("-");
  await speaker.waitForFunction(() => document.documentElement.dataset.fontScale === "0.95" &&
    [...document.querySelectorAll("iframe")].every((frame) => frame.contentDocument.documentElement.dataset.fontScale === "0.95"));
  await speaker.keyboard.press("0");
  await page.waitForFunction(() => document.documentElement.dataset.fontScale === "1.00");

  await speaker.keyboard.press("t");
  await page.waitForFunction(() => !document.documentElement.dataset.theme);
  await speaker.waitForFunction(() => document.documentElement.dataset.theme === "dark" &&
    [...document.querySelectorAll("iframe")].every((frame) => !frame.contentDocument.documentElement.dataset.theme));
  await page.keyboard.press("t");
  await speaker.waitForFunction(() => document.documentElement.dataset.theme === "light" &&
    [...document.querySelectorAll("iframe")].every((frame) => frame.contentDocument.documentElement.dataset.theme === "light"));

  // L continua sendo o atalho de navegação nativo do Reveal.
  await page.keyboard.press("l");
  await page.waitForFunction(() => Reveal.getIndices().h === 1);
  await speaker.waitForFunction(() => document.querySelector(".speaker-controls-notes .value").textContent.includes("conceito"));
  await speaker.evaluate(() => { window.opener.__testSpeaker = window; });
  await speaker.close();
  await page.waitForFunction(() => window.__testSpeaker.closed);
  await page.bringToFront();
  const [reopened] = await Promise.all([page.waitForEvent("popup"), page.keyboard.press("s")]);
  await reopened.waitForFunction(() => document.documentElement.dataset.theme === "light" &&
    document.querySelectorAll("iframe").length === 2 &&
    [...document.querySelectorAll("iframe")].every((frame) => frame.contentWindow.Reveal?.isReady() && frame.contentDocument.documentElement.dataset.theme === "light"));
  await reopened.frameLocator("#current-slide iframe").locator("body").press("t");
  await page.waitForFunction(() => !document.documentElement.dataset.theme);
  await reopened.waitForFunction(() => document.documentElement.dataset.theme === "dark" &&
    [...document.querySelectorAll("iframe")].every((frame) => !frame.contentDocument.documentElement.dataset.theme));
  if (!withoutStorage) {
    await page.keyboard.press("+");
    await page.reload({ waitUntil: "networkidle" });
    await page.waitForFunction(() => Reveal.isReady() && !document.documentElement.dataset.theme && document.documentElement.dataset.fontScale === "1.05");
    await page.keyboard.press("t");
    await reopened.waitForFunction(() => document.documentElement.dataset.theme === "light" && document.documentElement.dataset.fontScale === "1.05" &&
      [...document.querySelectorAll("iframe")].every((frame) => frame.contentDocument.documentElement.dataset.theme === "light"));
  }
  assert.deepEqual(errors, []);
  await context.close();
}

(async () => {
  const browser = await chromium.launch();
  try {
    await testTheme(browser, false);
    await testTheme(browser, true);
    console.log("Tema e Speaker View sincronizados, com e sem armazenamento local.");
  } finally {
    await browser.close();
  }
})().catch((error) => { console.error(error); process.exitCode = 1; });
