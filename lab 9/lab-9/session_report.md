# Session Report

## Part 1: Code-Level Probe Session (measured)

| Metric | Value |
|--------|-------|
| Probes run | 24 |
| Probes that exposed an issue | 20 |
| Probes with expected behaviour | 4 (P03, P08, P12, P23) |
| Distinct issues found | 13 |
| High severity | 6 |
| Medium severity | 3 |
| Low severity | 4 |
| Already known from Lab 4 | 2 (DEF-01, DEF-02, re-confirmed by P15 and P14) |
| New issues | 11 |

Findings by AI idea: idea 1 (Structure): 1 issue; idea 2 (Function): 3; idea 3 (Data / Interfaces): 2; idea 4 (Platform): 3;
idea 5 (Operations / Time): 4. All 13 issues came from probes planned from the AI's ideas; one (the data loss in
`save_tasks`) was escalated by an unplanned follow-up probe (P24).

## Part 2: UI Session (to complete)

| Metric | Value |
|--------|-------|
| Total bugs found |  |
| AI-suggested |  |
| Self-found |  |
| High / Medium / Low |  |

## Conclusion
The AI ideas directed the exploration to areas that ordinary happy-path tests miss (shared defaults, duplicate ids,
persistence failures), and the most serious findings were all in those areas. The AI could not tell which
behaviours are intended: for example, whether silently ignoring an unknown id in `remove_task` is acceptable still
needs a human decision. Add your UI session results above to compare AI-suggested and self-found bugs.

## Recommended Follow-Up
1. Validate input in `add_task` (non-empty title, numeric priority).
2. Generate ids safely (for example `max(id) + 1`) so removal cannot create duplicates.
3. Write the file atomically in `save_tasks` (write to a temp file, then rename) and handle a corrupt file in `load_tasks`.
4. Use `tags=None` and create a new list inside `add_task`; use `with open(...)` in `load_tasks`.
