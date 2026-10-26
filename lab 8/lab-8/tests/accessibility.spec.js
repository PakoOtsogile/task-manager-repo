// Lab 8: accessibility scan with axe-core + Playwright.
// Run before fixing:  A11Y_STAGE=before npx playwright test tests/accessibility.spec.js
// Run after fixing:   A11Y_STAGE=after  npx playwright test tests/accessibility.spec.js
// Windows PowerShell: $env:A11Y_STAGE="before"; npx playwright test tests/accessibility.spec.js
const { test, expect } = require('@playwright/test');
const { AxeBuilder } = require('@axe-core/playwright');
const fs = require('fs');

const stage = process.env.A11Y_STAGE || 'before';

test('Homepage has no accessibility violations', async ({ page }) => {
  await page.goto('http://localhost:3000');
  const results = await new AxeBuilder({ page })
    .withTags(['wcag2a', 'wcag2aa'])
    .analyze();

  // Save the full list of violations so it can be submitted and triaged
  fs.writeFileSync(`accessibility_${stage}.json`, JSON.stringify(results.violations, null, 2));
  console.log(`${stage}: ${results.violations.length} violation type(s)`);
  for (const v of results.violations) {
    console.log(`- ${v.id} [${v.impact}] on ${v.nodes.length} element(s): ${v.help}`);
  }

  expect(results.violations).toEqual([]);
});
