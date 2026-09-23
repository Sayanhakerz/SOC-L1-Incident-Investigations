# Case 004 - Windows Event Log Investigation Timeline

| Time | Event | Evidence |
|---|---|---|
| T0 | Multiple failed network logons begin | Event ID 4625 |
| T1 | jsmith receives repeated failed authentication attempts | Event ID 4625 |
| T2 | administrator receives repeated failed authentication attempts | Event ID 4625 |
| T3 | jsmith successfully authenticates | Event ID 4624 |
| T4 | administrator successfully authenticates | Event ID 4624 |
| T5 | Successful sessions later terminate | Event ID 4634 |

## Source Analysis

The suspicious authentication activity originated from:

10.0.0.25

The source attempted authentication against multiple accounts.

## Authentication Sequence

10.0.0.25
    |
    +--> jsmith
    |      |
    |      +--> Multiple failed logons
    |      |
    |      +--> Successful logon
    |
    +--> administrator
           |
           +--> Multiple failed logons
           |
           +--> Successful logon

## Timeline Assessment

The supplied Windows Security Event Log evidence shows repeated authentication failures from the same source IP against multiple accounts, followed by successful authentication.

This pattern is suspicious and is consistent with possible password guessing or credential attack activity.

However, the evidence is synthetic and does not establish that a real attack occurred.

No conclusion about actual compromise should be made from this training dataset alone.

## Evidence Classification

Synthetic / Lab-Generated.
