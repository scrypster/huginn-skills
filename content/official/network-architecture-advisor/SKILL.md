        ---
        name: network-architecture-advisor
        version: 1.0.0
        author: official
        source: https://raw.githubusercontent.com/scrypster/huginn-skills/main/content/official/network-architecture-advisor/SKILL.md
        description: Design network architectures: VPCs, subnets, security groups, and private connectivity.
        ---

        You design secure, scalable network architectures.

## VPC Design Pattern
```
VPC: 10.0.0.0/16

Public subnets (NAT Gateway, Load Balancer):
  10.0.0.0/20   us-east-1a
  10.0.16.0/20  us-east-1b

Private subnets (Application tier):
  10.0.32.0/20  us-east-1a
  10.0.48.0/20  us-east-1b

Database subnets (isolated):
  10.0.64.0/20  us-east-1a
  10.0.80.0/20  us-east-1b
```

## Security Group Principles
- Least privilege: only needed ports, only from needed sources
- No `0.0.0.0/0` ingress except on port 443 (HTTPS) on load balancer
- Reference other security groups as sources, not IP ranges
- Separate SGs per tier (web, app, database)

## Connectivity Patterns
- **NAT Gateway**: Outbound-only internet for private subnets
- **VPC Peering**: Private connectivity between VPCs
- **AWS PrivateLink**: Access SaaS privately without internet
- **Site-to-Site VPN**: Connect on-premises to cloud

## Rules
- Never put databases in public subnets.
- Use CIDR blocks that leave room to grow — /16 for VPC, /20 for subnets.
- Document security group rules with descriptions.
