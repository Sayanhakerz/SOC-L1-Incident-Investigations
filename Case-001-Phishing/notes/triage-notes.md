# Case 001 — Initial Triage Notes

## Alert

Potential phishing email impersonating Microsoft Support.

## Initial Observations

### 1. Displayed Sender

```text
support@micros0ft-security.example
```

The domain is suspicious because `micros0ft` uses the number `0` instead of the letter `o`.

### 2. Reply-To

```text
verify-account@secure-m365-login.example
```

The Reply-To address uses a different domain from the sender.

### 3. Return-Path

```text
bounce@micros0ft-security.example
```

### 4. Received Header

```text
mail.micros0ft-security.example
198.51.100.25
```

### 5. Authentication

```text
SPF: FAIL
DKIM: FAIL
DMARC: FAIL
```

### 6. URL

```text
https://micros0ft-security.example/login
```

The URL requests account verification.

## Social Engineering Indicators

- Urgent language
- Account suspension threat
- Request for immediate verification
- Microsoft impersonation

## User Interaction

No evidence of the recipient clicking the URL is available in the current dataset.

## Initial Assessment

The combination of a lookalike sender domain, separate Reply-To domain, authentication failures, and credential-verification URL indicates a likely phishing attempt.

Further investigation is required before final classification.

## Evidence Classification

Synthetic / Lab-Generated
