# Web API Workflow Triggers and Events

This document defines the workflow triggers and events for our web API automation architecture with GitHub Actions.

## Workflow Triggers

GitHub Actions workflows can be triggered by various events. For our web API automation, we'll use the following triggers:

### 1. Push Events

Workflows triggered when code is pushed to specific branches:

```yaml
on:
  push:
    branches:
      - main          # Production deployment pipeline
      - develop       # Development deployment pipeline
      - 'feature/**'  # Feature branch testing
    paths:
      - 'src/**'      # Only trigger when source code changes
      - 'api/**'      # API definition changes
      - '.github/workflows/**' # Workflow file changes
```

### 2. Pull Request Events

Workflows triggered when pull requests are created or updated:

```yaml
on:
  pull_request:
    types:
      - opened        # New PR created
      - synchronize   # PR updated with new commits
      - reopened      # Closed PR reopened
    branches:
      - main          # PRs targeting main branch
      - develop       # PRs targeting develop branch
    paths:
      - 'src/**'      # Only trigger when source code changes
      - 'api/**'      # API definition changes
```

### 3. Scheduled Events

Workflows that run on a regular schedule:

```yaml
on:
  schedule:
    - cron: '0 0 * * *'  # Daily at midnight UTC for health checks
    - cron: '0 2 * * 1'  # Weekly on Monday at 2:00 UTC for security scans
    - cron: '0 3 1 * *'  # Monthly on the 1st at 3:00 UTC for performance tests
```

### 4. Manual Dispatch

Workflows that can be triggered manually:

```yaml
on:
  workflow_dispatch:
    inputs:
      environment:
        description: 'Environment to deploy to'
        required: true
        default: 'development'
        type: choice
        options:
          - development
          - staging
          - production
      version:
        description: 'Version to deploy'
        required: false
        type: string
```

### 5. Repository Dispatch

Workflows triggered by external events:

```yaml
on:
  repository_dispatch:
    types:
      - deploy-command     # External deployment trigger
      - rollback-command   # External rollback trigger
      - api-test-command   # External API test trigger
```

## Event Filtering

For more granular control, we'll use event filtering:

### Path Filtering

```yaml
on:
  push:
    paths:
      - 'src/**'
      - 'api/**'
      - 'tests/**'
      - 'package.json'
      - 'package-lock.json'
      - '.github/workflows/**'
    paths-ignore:
      - '**.md'
      - 'docs/**'
```

### Branch Filtering with Patterns

```yaml
on:
  push:
    branches:
      - main
      - 'release/**'
      - 'feature/**'
      - '!feature/experimental/**'  # Exclude experimental features
```

## Conditional Execution

We'll use conditional execution to control when specific jobs or steps run:

```yaml
jobs:
  deploy:
    if: github.event_name == 'push' && github.ref == 'refs/heads/main'
    runs-on: ubuntu-latest
    steps:
      # Deployment steps

  test:
    if: github.event_name == 'pull_request' || github.ref != 'refs/heads/main'
    runs-on: ubuntu-latest
    steps:
      # Testing steps
```

## Environment-Specific Workflows

Different environments will have different workflow configurations:

### Development Environment

- Triggered on push to develop branch
- Automated deployment without approval
- Full test suite execution
- Development-specific configuration

### Staging Environment

- Triggered on push to release branches
- Requires approval from QA team
- Full test suite execution
- Staging-specific configuration

### Production Environment

- Triggered on push to main branch
- Requires approval from release manager
- Smoke tests only
- Production-specific configuration

## Advanced Trigger Patterns

### API Contract Testing

```yaml
on:
  push:
    paths:
      - 'api/openapi.yaml'  # API specification changes
      - 'api/schema/**'     # Schema changes
```

### Database Migration Workflows

```yaml
on:
  push:
    paths:
      - 'migrations/**'     # Database migration scripts
```

### Documentation Updates

```yaml
on:
  push:
    paths:
      - 'docs/**'           # Documentation changes
    branches:
      - main
```

## Integration with External Systems

### Webhook-Triggered Workflows

```yaml
on:
  repository_dispatch:
    types:
      - external-system-event
```

### Scheduled API Health Checks

```yaml
on:
  schedule:
    - cron: '*/15 * * * *'  # Every 15 minutes
```

## Conclusion

This comprehensive set of workflow triggers and events provides a flexible and powerful foundation for our web API automation architecture. By leveraging these triggers appropriately, we can ensure that the right workflows run at the right time, optimizing both resource usage and developer experience.
