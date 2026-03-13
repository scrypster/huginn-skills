        ---
        name: kubernetes-expert
        version: 1.0.0
        author: official
        source: https://raw.githubusercontent.com/scrypster/huginn-skills/main/content/official/kubernetes-expert/SKILL.md
        description: Write production Kubernetes manifests: deployments, services, probes, and HPA.
        ---

        You write production-ready Kubernetes manifests.

## Deployment Template
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: api
spec:
  replicas: 3
  selector:
    matchLabels:
      app: api
  template:
    spec:
      containers:
      - name: api
        image: myapp:1.2.3
        ports:
        - containerPort: 8080
        resources:
          requests:
            cpu: 100m
            memory: 128Mi
          limits:
            cpu: 500m
            memory: 256Mi
        livenessProbe:
          httpGet:
            path: /healthz
            port: 8080
          initialDelaySeconds: 10
          periodSeconds: 10
        readinessProbe:
          httpGet:
            path: /ready
            port: 8080
          initialDelaySeconds: 5
        securityContext:
          runAsNonRoot: true
          allowPrivilegeEscalation: false
```

## Rules
- Always set resource requests AND limits.
- Always add liveness and readiness probes.
- Never run as root in containers.
- Use `RollingUpdate` strategy with maxUnavailable=0 for zero-downtime.
