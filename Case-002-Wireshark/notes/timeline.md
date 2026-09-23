# Case 002 — Investigation Timeline

| Time (relative) | Event | Evidence |
|---|---|---|
| 0.000000 | Internal host sends DNS query for `update-check.example` | DNS packet |
| 0.000571 | DNS response received | DNS response |
| 0.000980 | TCP SYN sent from `10.0.0.50` to `198.51.100.50:80` | TCP packet |
| 0.001139 | TCP response received from `198.51.100.50:80` | TCP packet |
| 0.001261 | TCP ACK sent by internal host | TCP packet |
| 0.001372 | HTTP `GET /update` request sent | HTTP packet |
| 0.001591 | HTTP/TCP response received | TCP/HTTP packet |

## Timeline Assessment

The traffic follows a consistent network sequence:

DNS query → DNS response → TCP connection → HTTP request → HTTP response.

The internal host `10.0.0.50` successfully communicated with
`198.51.100.50` over HTTP and requested `/update`.

The PCAP does not contain sufficient evidence to determine whether
malicious code was executed on the internal host.
