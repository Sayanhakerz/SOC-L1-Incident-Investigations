# Case 002 — IOC Analysis

| IOC Type | Indicator | Finding | Confidence |
|---|---|---|---|
| Internal IP | 10.0.0.50 | Internal host generating the observed traffic | High |
| Domain | update-check.example | Domain queried through DNS | High |
| IP Address | 198.51.100.50 | IP returned by DNS and contacted over HTTP | High |
| URL | http://update-check.example/update | HTTP resource requested by internal host | High |
| Protocol | HTTP | Unencrypted web communication observed | High |
| Destination Port | 80/TCP | HTTP destination port | High |

## Network Sequence

```text
10.0.0.50
    |
    | DNS query
    v
update-check.example
    |
    | DNS response
    v
198.51.100.50
    |
    | TCP/80
    v
HTTP GET /update
