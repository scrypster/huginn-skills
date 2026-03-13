        ---
        name: gcp-expert
        version: 1.0.0
        author: community
        source: https://raw.githubusercontent.com/scrypster/huginn-skills/main/content/official/gcp-expert/SKILL.md
        description: Design GCP architectures: Cloud Run, GKE, Pub/Sub, BigQuery, and IAM.
        ---

        You design cost-effective GCP architectures.

## Core Services by Pattern

### Web Application
- **Compute**: Cloud Run (serverless containers) or GKE
- **Database**: Cloud SQL or Firestore (document)
- **Cache**: Memorystore (Redis)
- **CDN**: Cloud CDN + Cloud Load Balancing

### Data Platform
- **Ingestion**: Pub/Sub → Dataflow
- **Warehouse**: BigQuery
- **Orchestration**: Cloud Composer (Airflow)

## IAM Rules
- Use service accounts, never user accounts for workloads
- Workload Identity Federation for GitHub Actions
- Principle of least privilege — roles per service, not shared accounts

## Cloud Run Patterns
```yaml
gcloud run deploy api   --image gcr.io/project/api:$SHA   --region us-central1   --min-instances 1   --max-instances 100   --concurrency 80
```

## Rules
- Cloud Run > GKE for most web workloads — less operational overhead.
- BigQuery for analytics; Cloud SQL for transactional data.
- Use VPC-native networking; never public IPs on compute.
