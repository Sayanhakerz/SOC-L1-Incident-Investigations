# Case 002 — Wireshark Triage Notes

## Alert Type
Suspicious network traffic

## Initial Alert
A network traffic capture was provided for investigation. The objective
was to identify suspicious DNS, TCP, and HTTP activity and determine
whether the observed communication represents a security incident.

## Initial Observations

1. Internal host `10.0.0.50` generated a DNS query for:
   `update-check.example`

2. DNS response resolved the domain to:
   `198.51.100.50`

3. The internal host then established TCP communication with:
   `198.51.100.50:80`

4. HTTP traffic was observed using:
   `GET /update HTTP/1.1`

5. The HTTP Host header was:
   `update-check.example`

6. The HTTP response returned:
   `HTTP/1.1 200 OK`

7. The HTTP response contained:
   `Update service response`

## Initial Assessment

The traffic shows a clear sequence:

DNS query → DNS response → TCP connection → HTTP request → HTTP response.

The communication is suspicious because an internal host contacted an
external address over HTTP and requested an update resource.

However, the available PCAP does not provide sufficient evidence to
prove malware execution or compromise.

## Evidence Classification

This is a synthetic/lab-generated PCAP created for SOC training.

The domain and IP addresses are documentation/test indicators and
should not be treated as real malicious infrastructure.
