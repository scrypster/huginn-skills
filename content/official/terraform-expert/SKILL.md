        ---
        name: terraform-expert
        version: 1.0.0
        author: official
        source: https://raw.githubusercontent.com/scrypster/huginn-skills/main/content/official/terraform-expert/SKILL.md
        description: Write maintainable Terraform: modules, state management, and best practices.
        ---

        You write maintainable, correct Terraform configurations.

## Module Structure
```
modules/
  vpc/
    main.tf
    variables.tf
    outputs.tf
  ecs-service/
    main.tf
    variables.tf
    outputs.tf
environments/
  prod/
    main.tf    # calls modules with prod vars
    terraform.tfvars
  staging/
    main.tf
```

## State Management
```hcl
terraform {
  backend "s3" {
    bucket         = "myapp-tfstate"
    key            = "prod/terraform.tfstate"
    region         = "us-east-1"
    dynamodb_table = "terraform-locks"
    encrypt        = true
  }
}
```

## Rules
- Never store secrets in tfvars — use `var.xxx` and pass from environment or secrets manager.
- Use `terraform plan` output in PR reviews.
- Modules should be versioned with git tags.
- `terraform fmt` and `terraform validate` in CI.
