# AI-Generated RTM Comparison

## Step 1: Prompt Used

The following prompt was used to generate an RTM with AI:

> I have these requirements for a Task Manager application:
>
> REQ-01: Add a new task  
> REQ-02: Mark task complete  
> REQ-03: Get pending tasks  
> REQ-04: Average priority  
> REQ-05: Premium discount  
> REQ-06: Persist tasks to disk
>
> Generate a requirements traceability matrix with test case IDs.

## Step 2: Comparison

| Requirement | Your RTM | AI RTM | Divergence |
|---|---|---|---|
| REQ-01 | TC-01, TC-02 | TC-01 | AI missed priority variant |
| REQ-02 | TC-03, TC-04 | TC-02 | AI missed invalid ID case |
| REQ-03 | TC-05, TC-06 | TC-03 | AI missed empty list case |
| REQ-04 | TC-07, TC-08 | TC-04 | AI missed empty list case |
| REQ-05 | TC-09, TC-10 | TC-05, TC-06 | Complete |
| REQ-06 | TC-11, TC-12 | Not covered | AI missed persistence entirely |

## Analysis

The AI-generated RTM was incomplete compared with the manual RTM supplied in this lab.

The main differences were:

1. **REQ-01:** The AI did not include the priority variant.
2. **REQ-02:** The AI did not include the invalid-ID case.
3. **REQ-03:** The AI did not include the empty-list case.
4. **REQ-04:** The AI did not include the empty-list case.
5. **REQ-05:** The AI covered the requirement completely.
6. **REQ-06:** The AI did not cover task persistence at all.

## Conclusion

The comparison shows that AI can generate an initial RTM quickly, but the generated matrix should be reviewed against the requirements. In this lab, the manual RTM provided broader coverage because it included edge cases and persistence testing.
