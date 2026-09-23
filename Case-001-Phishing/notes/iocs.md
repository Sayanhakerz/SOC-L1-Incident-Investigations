# Case 001 — IOC Analysis

| IOC Type | Indicator | Finding | Confidence |
|---|---|---|---|
| Email Address | support@micros0ft-security.example | Suspicious sender | High |
| Email Address | verify-account@secure-m365-login.example | Suspicious Reply-To | High |
| Domain | micros0ft-security.example | Lookalike sender domain | High |
| Domain | secure-m365-login.example | Separate verification domain | High |
| IP Address | 198.51.100.25 | Synthetic sending IP from lab evidence | Medium |
| URL | https://micros0ft-security.example/login | Credential-verification URL | High |

## Authentication Indicators

- SPF: FAIL
- DKIM: FAIL
- DMARC: FAIL

## Suspicious Characteristics

- Lookalike domain
- Microsoft impersonation
- Different Reply-To domain
- Credential-verification URL
- Urgency
- Account suspension threat

## Evidence Classification

All indicators in this case are **synthetic/lab-generated** and are intended for SOC training purposes.

The IP address and domains are documentation/test values and should not be treated as real malicious infrastructure.
