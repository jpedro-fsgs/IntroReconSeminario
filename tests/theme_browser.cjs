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

  const [speaker] = await Promise.all([page.waitForEvent("popup"), page.keyboard.press("s")]);
  speaker.on("pageerror", (error) => errors.push(error.message));
  await speaker.waitForFunction(() => document.documentElement.dataset.theme === "light" &&
    document.querySelectorAll("iframe").length === 2 &&
    [...document.querySelectorAll("iframe")].every((frame) => frame.contentWindow.Reveal?.isReady() && frame.contentDocument.documentElement.dataset.theme === "light"));

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
    await page.reload({ waitUntil: "networkidle" });
    await page.waitForFunction(() => Reveal.isReady() && !document.documentElement.dataset.theme);
    await page.keyboard.press("t");
    await reopened.waitForFunction(() => document.documentElement.dataset.theme === "light" &&
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
