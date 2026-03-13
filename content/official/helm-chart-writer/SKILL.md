        ---
        name: helm-chart-writer
        version: 1.0.0
        author: community
        source: https://raw.githubusercontent.com/scrypster/huginn-skills/main/content/official/helm-chart-writer/SKILL.md
        description: Write maintainable Helm charts with sane defaults and documented values.
        ---

        You write maintainable, production-ready Helm charts.

## Chart Structure
```
mychart/
  Chart.yaml        # metadata
  values.yaml       # defaults
  templates/
    deployment.yaml
    service.yaml
    ingress.yaml
    configmap.yaml
    _helpers.tpl    # named templates
```

## values.yaml Pattern
```yaml
image:
  repository: myapp
  tag: latest
  pullPolicy: IfNotPresent

replicaCount: 2

resources:
  requests:
    cpu: 100m
    memory: 128Mi
  limits:
    cpu: 500m
    memory: 256Mi

autoscaling:
  enabled: false
  minReplicas: 2
  maxReplicas: 10
```

## Rules
- Every value in values.yaml must be used or documented.
- Use `required` function for values that have no sane default.
- Run `helm lint` in CI.
- Provide an `NOTES.txt` with post-install instructions.
