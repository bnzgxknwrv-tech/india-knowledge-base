const { chromium } = require('playwright');
const path = require('path');

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  const htmlPath = 'file://' + path.resolve(__dirname, 'kumaon_dayplan_source.html');
  await page.goto(htmlPath, { waitUntil: 'networkidle' });
  await page.pdf({
    path: path.resolve(__dirname, 'Kumaon_Dagplan_19_29_December_2026.pdf'),
    format: 'A4',
    printBackground: true,
    margin: { top: '0', bottom: '0', left: '0', right: '0' },
  });
  await browser.close();
  console.log('PDF written');
})();
