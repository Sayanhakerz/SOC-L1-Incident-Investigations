# Case 001 — Phishing Email Investigation

## Case Information

| Field | Details |
|---|---|
| Case ID | EMAIL-2026-001 |
| Alert Type | Suspicious Email / Potential Phishing |
| Severity | Medium |
| Analyst Level | L1 SOC Analyst |
| Status | Escalated |
| Evidence Type | Synthetic / Lab-Generated |

---

## Executive Summary

A suspicious email claiming to be from Microsoft Support was investigated as part of a controlled SOC training exercise.

The email attempted to create urgency by claiming that the recipient's Microsoft 365 account would be suspended within 24 hours unless account verification was completed.

Multiple indicators were identified, including:

- Lookalike sender domain
- Different Reply-To domain
- SPF authentication failure
- DKIM authentication failure
- DMARC authentication failure
- Credential-verification URL

Based on the available evidence, the alert was classified as a **TRUE POSITIVE — PHISHING**.

No evidence of user interaction with the URL is available in the current dataset.

---

## Alert Details

### Sender

```text
support@micros0ft-security.example
```

The sender domain uses `micros0ft` instead of the legitimate `microsoft` spelling.

The use of `0` instead of `o` is a common lookalike-domain technique.

### Reply-To

```text
verify-account@secure-m365-login.example
```

The Reply-To address uses a different domain from the displayed sender.

This is suspicious because replies may be redirected to an address controlled by another domain.

### Return-Path

```text
bounce@micros0ft-security.example
```

### Sending Host

```text
mail.micros0ft-security.example
```

### Sending IP

```text
198.51.100.25
```

This IP address is part of a documentation/test range and is used only for this synthetic laboratory scenario.

---

## Authentication Analysis

The email contained the following authentication results:

```text
SPF: FAIL
DKIM: FAIL
DMARC: FAIL
```

The authentication failures increase confidence that the message should not be treated as a legitimate Microsoft communication.

---

## Suspicious URL

The email contained the following URL:

```text
https://micros0ft-security.example/login
```

The URL requests account verification and uses the same lookalike domain as the sender.

No evidence is available showing that the recipient clicked the URL.

---

## Initial Triage Findings

The following observations were made during initial triage:

1. The sender claims to represent Microsoft Support.
2. The sender domain is a lookalike domain.
3. The letter `o` in `microsoft` has been replaced with `0`.
4. The Reply-To address uses a different domain.
5. SPF authentication failed.
6. DKIM authentication failed.
7. DMARC authentication failed.
8. The message contains an account-verification URL.
9. The email uses urgency and a threat of account suspension.
10. No evidence of user interaction is available.

---

## Timeline

| Time (UTC) | Event |
|---|---|
| 09:14:02 | Email received by employee01@company.local |
| 09:14:02 | Sending host identified as mail.micros0ft-security.example |
| 09:14:02 | Sending IP identified as 198.51.100.25 |
| 09:14:02 | SPF authentication failed |
| 09:14:02 | DKIM authentication failed |
| 09:14:02 | DMARC authentication failed |
| 09:14:02 | Credential-verification URL identified |

---

## Indicators of Compromise

| IOC Type | Indicator | Finding | Confidence |
|---|---|---|---|
| Email Address | support@micros0ft-security.example | Suspicious sender | High |
| Email Address | verify-account@secure-m365-login.example | Suspicious Reply-To | High |
| Domain | micros0ft-security.example | Lookalike sender domain | High |
| Domain | secure-m365-login.example | Separate verification domain | High |
| IP Address | 198.51.100.25 | Synthetic sending IP | Medium |
| URL | https://micros0ft-security.example/login | Credential-verification URL | High |

---

## Analysis

The email contains multiple independent indicators associated with phishing.

The sender domain attempts to visually resemble Microsoft while using a different domain.

The Reply-To address redirects communication to another domain.

Email authentication controls failed for SPF, DKIM, and DMARC.

The message also uses urgency and an account-suspension threat to encourage the recipient to visit a credential-verification URL.

The combination of these indicators provides sufficient evidence to classify the alert as phishing within this controlled laboratory scenario.

---

## Verdict

**TRUE POSITIVE — PHISHING**

Confidence: **High**

Reason:

- Lookalike sender domain
- Suspicious Reply-To domain
- SPF failure
- DKIM failure
- DMARC failure
- Credential-verification URL
- Urgency/account-suspension social engineering

---

## Escalation Note

**Escalate to L2 SOC / Incident Response for further investigation.**

Recommended follow-up actions:

1. Search mail logs for additional recipients of the same message.
2. Search for other messages using the same sender and domains.
3. Check DNS, proxy, and web gateway logs for connections to the URL/domain.
4. Determine whether any users clicked the URL.
5. If a user interacted with the URL, investigate the affected endpoint.
6. If credentials were submitted, initiate the organization's credential-reset procedure.
7. Block confirmed malicious indicators according to organizational policy.
8. Search for related phishing messages or lookalike domains.

---

## Evidence Classification

All indicators and artifacts in this case are **synthetic/lab-generated** and are intended for SOC training and portfolio purposes.

The domains and IP address in this case should not be treated as real malicious infrastructure.

---

## Analyst Conclusion

The available evidence supports classification of this alert as a **TRUE POSITIVE — PHISHING**.

The investigation demonstrates an L1 SOC workflow involving:

- Alert triage
- Email header analysis
- Authentication-result analysis
- URL identification
- IOC extraction
- Timeline construction
- Verdict determination
- Escalation to L2 SOC / Incident Response
