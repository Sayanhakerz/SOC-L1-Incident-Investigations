# Case 004 - L1 SOC Triage Assessment

## Alert Type

Suspicious Authentication Activity

## Evidence Type

Synthetic / Lab-Generated Windows Security Event Logs

## Initial Observation

Multiple failed network logons were observed from the same source IP
against multiple user accounts.

Source IP:

10.0.0.25

## Authentication Findings

- `jsmith` had 5 failed logon attempts followed by a successful logon.
- `administrator` had 3 failed logon attempts followed by a successful logon.
- The suspicious authentication events used Logon Type 3 (Network Logon).
- The successful authentications occurred after repeated failures.

## L1 Assessment

The authentication pattern is suspicious and may be consistent with
password guessing or credential attack activity.

The repeated failures against multiple accounts from the same source,
followed by successful authentication, warrant investigation.

However, this evidence is synthetic and does not establish that a real
attack or compromise occurred.

## Severity

Medium

## Verdict

SUSPICIOUS AUTHENTICATION ACTIVITY - INCONCLUSIVE

## Recommended L2 Actions

1. Validate the source host associated with `10.0.0.25`.
2. Review endpoint telemetry for the source system.
3. Determine whether the successful logons were authorized.
4. Review authentication activity around the same time window.
5. Check for additional accounts targeted by the source.
6. Review Windows process and network telemetry.
7. Check whether any suspicious activity followed the successful logons.

## Analyst Conclusion

The supplied evidence demonstrates a suspicious authentication pattern
involving repeated failed network logons followed by successful
authentication against multiple accounts.

The evidence should be escalated for additional validation in a real
environment.

Because this is a synthetic training dataset, the case cannot be used
to establish a confirmed real-world compromise.
