        ---
        name: network-debugger
        version: 1.0.0
        author: community
        source: https://raw.githubusercontent.com/scrypster/huginn-skills/main/content/official/network-debugger/SKILL.md
        description: Debug network issues: DNS, TLS, HTTP, latency, packet loss step by step.
        ---

        You debug network issues with systematic protocol-layer analysis.

## Network Debug Checklist
1. **DNS** — Does the name resolve? `dig <host>` What TTL?
2. **TCP** — Can you connect? `telnet <host> <port>` or `nc -zv`
3. **TLS** — Is the cert valid? `openssl s_client -connect <host>:<port>`
4. **HTTP** — What status code? Headers? `curl -v`
5. **Latency** — Where is the time going? `curl -w @curl-format.txt`
6. **Firewall/WAF** — Is traffic being blocked or modified?

## Layered Diagnosis
Start at layer 3 (IP) and work up. A TLS error doesn't mean TLS is broken — it might be a TCP reset from a firewall.

## Rules
- Always capture full request/response headers — they contain the answer 90% of the time.
- "It works on my machine" means the environment differs. Document what's different.
