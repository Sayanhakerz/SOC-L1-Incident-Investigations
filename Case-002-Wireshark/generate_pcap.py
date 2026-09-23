from scapy.all import *
from datetime import datetime, timezone

packets = []

# Lab hosts / documentation addresses
client = "10.0.0.50"
dns_server = "10.0.0.53"
suspicious_ip = "198.51.100.50"
benign_ip = "198.51.100.60"

# -----------------------------
# 1. DNS query
# -----------------------------

dns_query = (
    IP(src=client, dst=dns_server)
    / UDP(sport=53000, dport=53)
    / DNS(
        id=1001,
        rd=1,
        qd=DNSQR(qname="update-check.example", qtype="A")
    )
)

packets.append(dns_query)

# DNS response
dns_response = (
    IP(src=dns_server, dst=client)
    / UDP(sport=53, dport=53000)
    / DNS(
        id=1001,
        qr=1,
        aa=1,
        rd=1,
        ra=1,
        qd=DNSQR(qname="update-check.example", qtype="A"),
        an=DNSRR(
            rrname="update-check.example",
            type="A",
            ttl=300,
            rdata=suspicious_ip
        )
    )
)

packets.append(dns_response)

# -----------------------------
# 2. TCP connection to resolved IP
# -----------------------------

client_port = 49152

syn = (
    IP(src=client, dst=suspicious_ip)
    / TCP(sport=client_port, dport=80, flags="S", seq=1000)
)

syn_ack = (
    IP(src=suspicious_ip, dst=client)
    / TCP(
        sport=80,
        dport=client_port,
        flags="SA",
        seq=2000,
        ack=1001
    )
)

ack = (
    IP(src=client, dst=suspicious_ip)
    / TCP(
        sport=client_port,
        dport=80,
        flags="A",
        seq=1001,
        ack=2001
    )
)

packets.extend([syn, syn_ack, ack])

# -----------------------------
# 3. HTTP request
# -----------------------------

http_request = (
    IP(src=client, dst=suspicious_ip)
    / TCP(
        sport=client_port,
        dport=80,
        flags="PA",
        seq=1001,
        ack=2001
    )
    / Raw(
        load=(
            b"GET /update HTTP/1.1\r\n"
            b"Host: update-check.example\r\n"
            b"User-Agent: Mozilla/5.0\r\n"
            b"Connection: close\r\n"
            b"\r\n"
        )
    )
)

packets.append(http_request)

# -----------------------------
# 4. HTTP response
# -----------------------------

http_response = (
    IP(src=suspicious_ip, dst=client)
    / TCP(
        sport=80,
        dport=client_port,
        flags="PA",
        seq=2001,
        ack=1200
    )
    / Raw(
        load=(
            b"HTTP/1.1 200 OK\r\n"
            b"Content-Type: text/html\r\n"
            b"Content-Length: 42\r\n"
            b"Connection: close\r\n"
            b"\r\n"
            b"<html>Update service response</html>"
        )
    )
)

packets.append(http_response)

# -----------------------------
# 5. Benign DNS query
# -----------------------------

benign_query = (
    IP(src=client, dst=dns_server)
    / UDP(sport=53001, dport=53)
    / DNS(
        id=2001,
        rd=1,
        qd=DNSQR(qname="ubuntu.com", qtype="A")
    )
)

packets.append(benign_query)

# -----------------------------
# 6. Benign DNS response
# -----------------------------

benign_response = (
    IP(src=dns_server, dst=client)
    / UDP(sport=53, dport=53001)
    / DNS(
        id=2001,
        qr=1,
        aa=1,
        rd=1,
        ra=1,
        qd=DNSQR(qname="ubuntu.com", qtype="A"),
        an=DNSRR(
            rrname="ubuntu.com",
            type="A",
            ttl=300,
            rdata=benign_ip
        )
    )
)

packets.append(benign_response)

# -----------------------------
# Write PCAP
# -----------------------------

output = "evidence/suspicious-traffic.pcap"

wrpcap(output, packets)

print(f"[+] Generated {len(packets)} packets")
print(f"[+] PCAP saved to: {output}")
