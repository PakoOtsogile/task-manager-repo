# Lab 9: Exploratory Testing with an AI Co-Pilot

## Completed By
- Student ID: <your ID>
- Date: <today's date>

## What I Did
1. Wrote a test charter (`charter.md`)
2. Asked an AI assistant for five SFDIPOT exploratory ideas (`session_notes.md`)
3. Turned the ideas into 24 probes against `app/tasks.py` and ran them (`probe_session.py`, `probe_output.txt`)
4. Logged 13 issues with severity and summarised them (`session_report.md`)
5. Left a template for the timed UI session, which needs the running app

## Key Findings
- 13 issues: 6 High, 3 Medium, 4 Low (2 already known from Lab 4)
- Most serious: a failed `save_tasks` leaves a half-written `tasks.json` and loses the previous data; duplicate ids after
  removing a task make `complete_task` hit the wrong task; a corrupt `tasks.json` stops the app loading

## Notes
- Part 1 is a scripted probe run, not a 45-minute human session. The 45-minute timed session and the AI-suggested vs
  self-found split must come from your own UI session (Part 2 of `session_notes.md`).
- To reproduce: put `probe_session.py` in your repo root (next to `app/`) and run `python probe_session.py`.
