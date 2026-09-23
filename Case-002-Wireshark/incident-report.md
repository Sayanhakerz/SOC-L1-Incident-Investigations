# Case 002 — Wireshark Network Traffic Investigation

## Case Information

| Field | Details |
|---|---|
| Case ID | NET-2026-002 |
| Alert Type | Suspicious Network Traffic |
| Analyst Level | L1 SOC Analyst |
| Severity | Medium |
| Status | Escalated |
| Evidence Type | Synthetic / Lab-Generated |
| Investigation Tool | Wireshark |
| Evidence File | suspicious-traffic.pcap |

---

## Executive Summary

A network packet capture was investigated after suspicious communication was observed between an internal host and an external IP address.

The investigation identified a complete communication sequence consisting of a DNS query, DNS response, TCP connection, HTTP request, and HTTP response.

The internal host `10.0.0.50` queried `update-check.example`, which resolved to `198.51.100.50`. The host subsequently established a TCP connection to port 80 and requested `/update` using HTTP.

The available evidence confirms network communication with the identified host but does not provide sufficient evidence to confirm malware execution, persistence, or host compromise.

---

## Alert Details

### Source Host

```text
10.0.0.50
```

### Destination IP

```text
198.51.100.50
```

### DNS Server

```text
10.0.0.53
```

### Domain

```text
update-check.example
```

### Protocols Observed

```text
DNS
TCP
HTTP
```

### Destination Port

```text
80/TCP
```

### Source Port

```text
49152/TCP
```

---

## Initial Triage

The PCAP was opened in Wireshark and reviewed to identify the source host, destination host, DNS activity, TCP communication, HTTP traffic, and potentially suspicious indicators.

The initial observations were:

1. Internal host `10.0.0.50` generated a DNS query for `update-check.example`.
2. DNS server `10.0.0.53` returned an A record pointing to `198.51.100.50`.
3. The internal host then initiated TCP communication with `198.51.100.50` on port 80.
4. A TCP connection was established.
5. The internal host sent an HTTP `GET /update` request.
6. The HTTP Host header identified `update-check.example`.
7. The external server returned an HTTP `200 OK` response.
8. The response contained:

```text
Update service response
```

9. The available PCAP does not show evidence proving malware execution, persistence, credential theft, or host compromise.

---

## DNS Analysis

The DNS transaction was identified in Wireshark.

### DNS Query

```text
Source:      10.0.0.50
Destination: 10.0.0.53
Protocol:    DNS
Query:       update-check.example
Query Type:  A
```

### DNS Response

```text
Source:      10.0.0.53
Destination: 10.0.0.50
Protocol:    DNS
Response:    198.51.100.50
```

The DNS response contained an A record mapping `update-check.example` to `198.51.100.50`.

---

## TCP Analysis

Following the DNS response, the internal host initiated a TCP connection to the resolved destination.

### TCP Connection

```text
Source:       10.0.0.50
Source Port:  49152
Destination:  198.51.100.50
Destination Port: 80
Protocol:     TCP
```

The packet capture showed TCP communication between the internal host and the external address before the HTTP request was transmitted.

The observed communication was:

```text
10.0.0.50:49152
        |
        | TCP
        v
198.51.100.50:80
```

---

## HTTP Analysis

The PCAP contained unencrypted HTTP traffic.

### HTTP Request

```text
GET /update HTTP/1.1
Host: update-check.example
User-Agent: Mozilla/5.0
Connection: close
```

### Full Request URL

```text
http://update-check.example/update
```

### HTTP Response

```text
HTTP/1.1 200 OK
Content-Type: text/html
Content-Length: 42
Connection: close
```

### Response Content

```text
Update service response
```

The HTTP response indicates that the remote server successfully returned content to the internal host.

However, the captured response does not demonstrate that an executable file or malicious payload was downloaded or executed.

---

## Network Communication Flow

The complete communication sequence observed in the PCAP was:

```text
10.0.0.50
     |
     | DNS Query
     | update-check.example
     v
10.0.0.53
     |
     | DNS Response
     | 198.51.100.50
     v
10.0.0.50
     |
     | TCP Connection
     | Port 80
     v
198.51.100.50
     |
     | HTTP GET /update
     v
198.51.100.50
     |
     | HTTP 200 OK
     | "Update service response"
     v
10.0.0.50
```

---

## Investigation Timeline

| Time (Relative) | Event | Evidence |
|---|---|---|
| 0.000000 | Internal host sends DNS query for `update-check.example` | DNS packet |
| 0.000571 | DNS response received | DNS response |
| 0.000980 | TCP SYN sent to `198.51.100.50:80` | TCP packet |
| 0.001139 | TCP response received | TCP packet |
| 0.001261 | TCP ACK sent by internal host | TCP packet |
| 0.001372 | HTTP GET `/update` request sent | HTTP packet |
| 0.001591 | HTTP/TCP response received | HTTP/TCP packet |

---

## IOC / Network Indicator Analysis

| IOC Type | Indicator | Finding | Confidence |
|---|---|---|---|
| Internal IP | `10.0.0.50` | Internal host generating the observed traffic | High |
| DNS Server | `10.0.0.53` | DNS server involved in resolution | High |
| Domain | `update-check.example` | Domain queried by the internal host | High |
| IP Address | `198.51.100.50` | IP returned by DNS and contacted over HTTP | High |
| URL | `http://update-check.example/update` | HTTP resource requested by the internal host | High |
| Protocol | HTTP | Unencrypted web communication observed | High |
| Destination Port | `80/TCP` | Standard HTTP destination port | High |

---

## Suspicious Indicators

### 1. External Communication

The internal host `10.0.0.50` communicated with the external address `198.51.100.50`.

### 2. HTTP Instead of HTTPS

The communication occurred over HTTP port 80 rather than encrypted HTTPS.

### 3. Update-Related Resource

The requested resource was:

```text
/update
```

The domain also used an update-related name:

```text
update-check.example
```

### 4. Complete DNS-to-HTTP Sequence

The traffic showed a clear sequence:

```text
DNS Query
    ↓
DNS Response
    ↓
TCP Connection
    ↓
HTTP Request
    ↓
HTTP Response
```

This demonstrates that the internal host successfully resolved the domain and communicated with the resulting IP address.

---

## Evidence Limitations

The PCAP provides network-level evidence only.

The capture does not contain sufficient evidence to determine:

- Which process initiated the connection
- Whether the user intentionally accessed the resource
- Whether a file was downloaded
- Whether an executable was downloaded
- Whether malware executed
- Whether persistence was established
- Whether credentials were stolen
- Whether the endpoint was compromised
- Whether the traffic was generated by legitimate software

Additional endpoint and security telemetry would therefore be required for a definitive determination.

---

## Assessment

The traffic is suspicious enough to warrant additional investigation because an internal host contacted an external IP address over unencrypted HTTP and requested an update-related resource.

The PCAP confirms that the communication occurred.

However, the available evidence does not independently prove that the activity was malicious.

There is no direct evidence in the capture of:

```text
Malware execution
Persistence
Credential theft
Command-and-control activity
Host compromise
```

Therefore, the PCAP alone is insufficient to classify the endpoint as compromised.

---

## Verdict

```text
SUSPICIOUS ACTIVITY — INCONCLUSIVE
```

### Verdict Explanation

The investigation confirmed suspicious network communication between the internal host and the identified external destination.

However, the available PCAP does not provide sufficient evidence to confirm malware execution, persistence, command-and-control activity, or host compromise.

The appropriate L1 SOC conclusion is therefore:

```text
Suspicious activity identified.
Further investigation required.
```

---

## Escalation Note

### Escalation Destination

```text
L2 SOC / Incident Response
```

### Escalation Reason

Escalation is recommended because the internal host communicated with an external destination over HTTP and requested an update-related resource.

Additional telemetry is required to determine whether the activity was legitimate or malicious.

### Recommended L2 Actions

1. Identify the endpoint associated with `10.0.0.50`.
2. Determine which process initiated the connection to `198.51.100.50`.
3. Review endpoint process creation and network connection logs.
4. Search DNS logs for additional queries to `update-check.example`.
5. Search proxy and firewall logs for connections to `198.51.100.50`.
6. Determine whether other internal hosts contacted the same domain or IP address.
7. Review endpoint security telemetry for downloaded files.
8. Check for suspicious process execution around the observed communication time.
9. If malicious activity is confirmed, contain the affected endpoint and block the confirmed indicators.

---

## Recommended Investigation Sources

The following sources should be reviewed during additional investigation:

```text
Endpoint Detection and Response (EDR)
DNS Logs
Proxy Logs
Firewall Logs
Web Gateway Logs
Windows Event Logs
Process Creation Logs
Network Connection Logs
Antivirus / EDR Alerts
```

---

## Evidence Classification

This investigation uses a synthetic/lab-generated PCAP created for SOC training and portfolio development.

The following indicators are documentation/test indicators:

```text
update-check.example
198.51.100.50
```

They should not be treated as real malicious infrastructure.

The internal addresses used in this lab are also synthetic:

```text
10.0.0.50
10.0.0.53
```

---

## Analyst Conclusion

The investigation demonstrated a standard L1 SOC network-triage workflow using Wireshark.

The analyst successfully identified:

```text
Source Host
     ↓
DNS Query
     ↓
DNS Response
     ↓
Resolved IP
     ↓
TCP Connection
     ↓
HTTP Request
     ↓
HTTP Response
     ↓
Network Indicators
     ↓
Timeline
     ↓
Assessment
     ↓
Verdict
     ↓
Escalation
```

The available evidence confirms suspicious network communication but does not independently establish endpoint compromise.

The case should therefore remain classified as:

```text
SUSPICIOUS ACTIVITY — INCONCLUSIVE
```

and be escalated to L2 SOC / Incident Response for additional validation.

---

## Case Status

```text
STATUS: ESCALATED
VERDICT: SUSPICIOUS ACTIVITY — INCONCLUSIVE
SEVERITY: MEDIUM
ANALYST LEVEL: L1 SOC
EVIDENCE: SYNTHETIC / LAB-GENERATED
TOOL: WIRESHARK
```
