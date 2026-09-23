# SOC-L1 Incident Investigation Report

## Case Information

| Field | Details |
|---|---|
| Case ID | AUTH-2026-004 |
| Alert Type | Suspicious Authentication Activity |
| Severity | Medium |
| Analyst Level | L1 SOC |
| Status | Closed - Lab Investigation |
| Evidence Type | Synthetic / Lab-Generated |
| Host | WIN-CLIENT-01 |
| Suspicious Source | 10.0.0.25 |

## Executive Summary

A Windows Security Event Log dataset was investigated for suspicious authentication activity.

Multiple failed network logons were observed from source IP 10.0.0.25 against multiple accounts. The activity included five failed logons against the jsmith account and three failed logons against the administrator account.

Successful authentication subsequently occurred for both accounts.

This authentication pattern is suspicious and may be consistent with password guessing or credential attack activity.

The evidence is synthetic and was created specifically for SOC training. It does not establish that a real attack or compromise occurred.

## Alert Details

The investigation focused on Windows Security Event IDs:

- 4625 - Failed logon
- 4624 - Successful logon
- 4634 - Logoff

The suspicious authentication events used:

Logon Type 3 - Network Logon

## Key Findings

### Source IP

10.0.0.25

This source generated repeated failed authentication attempts against multiple accounts.

### Account: jsmith

- 5 failed logon attempts
- Followed by successful authentication

### Account: administrator

- 3 failed logon attempts
- Followed by successful authentication

### Benign Comparison

Source IP 10.0.0.30 generated a successful interactive logon for the backupsvc account without preceding failed authentication attempts in the supplied evidence.

## Authentication Sequence

10.0.0.25
     |
     +--> jsmith
     |      |
     |      +--> 5 failed logons
     |      |
     |      +--> successful logon
     |
     +--> administrator
            |
            +--> 3 failed logons
            |
            +--> successful logon

## Investigation Timeline

| Stage | Event | Evidence |
|---|---|---|
| T0 | Failed network logons begin | Event ID 4625 |
| T1 | jsmith targeted by repeated failures | Event ID 4625 |
| T2 | administrator targeted by repeated failures | Event ID 4625 |
| T3 | jsmith successfully authenticates | Event ID 4624 |
| T4 | administrator successfully authenticates | Event ID 4624 |
| T5 | Sessions terminate | Event ID 4634 |

## IOC Summary

| IOC Type | Indicator | Description | Confidence |
|---|---|---|---|
| Source IP | 10.0.0.25 | Source of repeated authentication failures | High |
| Account | jsmith | Targeted account | High |
| Account | administrator | Targeted privileged account | High |
| Host | WIN-CLIENT-01 | Windows endpoint | High |
| Event ID | 4625 | Failed authentication | High |
| Event ID | 4624 | Successful authentication | High |
| Event ID | 4634 | Logoff | High |

## L1 Assessment

The observed authentication pattern is suspicious because the same source IP attempted authentication against multiple accounts and successful authentication occurred after repeated failures.

This behavior may indicate password guessing or credential attack activity.

The available evidence does not demonstrate what occurred after the successful authentications and does not independently establish account compromise.

## Verdict

**SUSPICIOUS AUTHENTICATION ACTIVITY - INCONCLUSIVE**

The evidence warrants further investigation but is insufficient to classify the activity as a confirmed compromise.

## Escalation Note

If this alert occurred in a real production environment, it should be escalated to L2 SOC / Incident Response for additional validation.

Recommended actions:

1. Identify the system associated with 10.0.0.25.
2. Determine whether the authentication attempts were authorized.
3. Review endpoint telemetry from the source host.
4. Review successful login activity for jsmith and administrator.
5. Search for additional accounts targeted by the same source.
6. Review process and network activity following successful logons.
7. Check for signs of privilege escalation or lateral movement.
8. Correlate the activity with other security alerts.

## Evidence Limitations

This investigation uses a synthetic Windows Security Event Log dataset created for SOC training.

The IP addresses, hostnames, usernames, and authentication events are lab-generated.

The evidence should not be interpreted as evidence of a real-world attack.

## Analyst Conclusion

The investigation identified a suspicious authentication pattern involving repeated failed network logons against multiple accounts from 10.0.0.25, followed by successful authentication.

The pattern warrants L2 investigation in a real environment.

Final classification:

**SUSPICIOUS AUTHENTICATION ACTIVITY - INCONCLUSIVE**

Evidence classification:

**SYNTHETIC / LAB-GENERATED**
