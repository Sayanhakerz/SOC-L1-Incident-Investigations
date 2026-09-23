# Case 001 — Investigation Timeline

| Time (UTC) | Event | Evidence |
|---|---|---|
| 09:14:02 | Email received by employee01@company.local | Email Date header |
| 09:14:02 | Email identified as originating from mail.micros0ft-security.example | Received header |
| 09:14:02 | Sending IP identified as 198.51.100.25 | Received header |
| 09:14:02 | SPF authentication failed | Received-SPF header |
| 09:14:02 | DKIM authentication failed | Authentication-Results |
| 09:14:02 | DMARC authentication failed | Authentication-Results |
| 09:14:02 | Credential-verification URL identified | Email body |

## Timeline Assessment

The available evidence shows that the suspicious email was received at 09:14:02 UTC and contained multiple authentication failures, a lookalike sender domain, a separate Reply-To domain, and a credential-verification URL.

No evidence of user interaction with the URL is available in the current dataset.

## Investigation Status

Final classification:

**TRUE POSITIVE — PHISHING**

Escalation:

**L2 SOC / Incident Response**
