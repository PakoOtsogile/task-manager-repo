# Lab 8: Visual Regression & Accessibility Testing

## Completed By
- Student ID: <your ID>
- Date: <today's date>

## Status
This folder holds the ready-to-run setup. The results (baseline images, diff report, scan output and triage) depend
on your running web app at `http://localhost:3000`, so they were not generated here and have not been invented.
Run the steps below, then fill in `triage_table.md` from the real output.

## Part A: Visual Regression (BackstopJS)
```bash
npm install -g backstopjs          # or: npx backstopjs ...
# put this folder's backstop.json in your project root; start your app on port 3000, then:
backstop reference                 # 1. capture the baseline (creates backstop_data/bitmaps_reference)
# 2. make a deliberate change, e.g. a CSS margin or font-size, and save it
backstop test                      # 3. compare; opens an HTML report with the pixel diff (backstop_data/)
```
Deliverables: `backstop.json`, `backstop_data/` (copy the folder after the run), and a note on what you changed and
what the diff showed (changed pixels, which viewport failed).

## Part B: Accessibility (axe-core + Playwright)
```bash
npm install -D @playwright/test @axe-core/playwright
npx playwright install
A11Y_STAGE=before npx playwright test tests/accessibility.spec.js   # creates accessibility_before.json (test fails if violations exist)
# fix two violations in your app, then:
A11Y_STAGE=after  npx playwright test tests/accessibility.spec.js   # creates accessibility_after.json
```
Then fill in `triage_table.md` with the violations your scan reported.

## Files
- `backstop.json`, `tests/accessibility.spec.js`, `triage_table.md` (provided here)
- `backstop_data/`, `accessibility_before.json`, `accessibility_after.json` (created when you run the steps)

## Check List
- [ ] Baseline captured with `backstop reference`
- [ ] Deliberate change made and `backstop test` diff report reviewed
- [ ] axe scan run before fixing
- [ ] Two violations fixed and scan re-run
- [ ] `triage_table.md` completed from real results
