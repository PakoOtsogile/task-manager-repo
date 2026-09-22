## Lab 1: Environment Setup & Manual Defect Hunting

## Completed By
- Student ID: <23017899>
- Date: <14/09/2026>

## What I Did
1. Installed Git, Python 3.11, VS Code, and configured a free-tier AI assistant
2. Cloned the sample task-manager repository
3. Ran the application and existing test suite
4. Manually read all source files and logged 10 defects
5. Recorded tool versions and test results

## Defects Found
- 10 defects total (see defect_log.md)
- Severity breakdown: 3 Critical, 3 High, 2 Medium, 2 Low

## Test Suite Results
- 6 tests total: 4 passed, 2 failed
- Failures confirm Defects D01 and D02

## Reflection
Manual reading revealed 8 defects that automated tests did NOT catch.
This demonstrates the value of human code review alongside tooling.