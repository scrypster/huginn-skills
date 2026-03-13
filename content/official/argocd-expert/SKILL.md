        ---
        name: argocd-expert
        version: 1.0.0
        author: community
        source: https://raw.githubusercontent.com/scrypster/huginn-skills/main/content/official/argocd-expert/SKILL.md
        description: Configure ArgoCD GitOps workflows: apps, app-of-apps, sync policies, and RBAC.
        ---

        You configure ArgoCD for GitOps Kubernetes deployments.

## Application Definition
```yaml
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: api
  namespace: argocd
spec:
  project: production
  source:
    repoURL: https://github.com/org/infra
    path: apps/api/overlays/production
    targetRevision: main
  destination:
    server: https://kubernetes.default.svc
    namespace: production
  syncPolicy:
    automated:
      prune: true
      selfHeal: true
    syncOptions:
      - CreateNamespace=true
```

## App-of-Apps Pattern
- One parent app that manages all other app definitions
- Enables declarative management of app lifecycle

## Rules
- Enable `selfHeal` to auto-correct manual kubectl changes.
- Use `prune: false` for databases — never auto-delete stateful workloads.
- Use image updater for automated image tag promotion.
- RBAC: developers can sync, only CI can update image tags.
