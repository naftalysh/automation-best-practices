# Web API Deployment Pipeline

This document outlines the deployment pipeline for our web API automation architecture with GitHub Actions.

## Deployment Environments

Our deployment pipeline supports multiple environments:

### 1. Development Environment

- **Purpose**: Testing new features and fixes
- **Deployment Frequency**: Continuous (on every merge to develop branch)
- **Approval Requirements**: None (automated)
- **Configuration**: Development-specific settings
- **URL Pattern**: `api-dev.example.com`

### 2. Staging Environment

- **Purpose**: Pre-production validation
- **Deployment Frequency**: On-demand or scheduled
- **Approval Requirements**: QA team approval
- **Configuration**: Production-like settings
- **URL Pattern**: `api-staging.example.com`

### 3. Production Environment

- **Purpose**: Live service for end users
- **Deployment Frequency**: Scheduled releases
- **Approval Requirements**: Release manager approval
- **Configuration**: Production settings
- **URL Pattern**: `api.example.com`

## Deployment Strategies

We implement several deployment strategies based on the environment and requirements:

### 1. Blue-Green Deployment

- **How it works**: Maintain two identical production environments (Blue and Green)
- **Process**:
  1. Deploy new version to inactive environment
  2. Run tests against the new deployment
  3. Switch traffic from active to inactive environment
  4. Keep old environment as fallback for quick rollback
- **Implementation**:
  ```yaml
  jobs:
    deploy:
      runs-on: ubuntu-latest
      steps:
        - uses: actions/checkout@v3
        - name: Determine target environment (blue/green)
          id: target
          run: |
            CURRENT=$(curl -s https://api.example.com/env)
            if [ "$CURRENT" = "blue" ]; then
              echo "target=green" >> $GITHUB_OUTPUT
            else
              echo "target=blue" >> $GITHUB_OUTPUT
            fi
        - name: Deploy to target environment
          run: |
            ./deploy.sh ${{ steps.target.outputs.target }}
        - name: Run smoke tests
          run: ./test.sh ${{ steps.target.outputs.target }}
        - name: Switch traffic
          run: ./switch.sh ${{ steps.target.outputs.target }}
  ```

### 2. Canary Deployment

- **How it works**: Gradually roll out changes to a small subset of users
- **Process**:
  1. Deploy new version alongside the current version
  2. Route a small percentage of traffic to the new version
  3. Monitor for errors and performance issues
  4. Gradually increase traffic to the new version
  5. Complete the rollout when confident
- **Implementation**:
  ```yaml
  jobs:
    canary_deploy:
      runs-on: ubuntu-latest
      steps:
        - uses: actions/checkout@v3
        - name: Deploy canary
          run: ./deploy_canary.sh
        - name: Route 5% traffic to canary
          run: ./route_traffic.sh 5
        - name: Monitor for 15 minutes
          run: ./monitor.sh 900
        - name: Route 20% traffic if healthy
          if: success()
          run: ./route_traffic.sh 20
        # Continue with incremental increases
  ```

### 3. Rolling Deployment

- **How it works**: Update instances one at a time
- **Process**:
  1. Take one instance out of the load balancer
  2. Update the instance
  3. Put the instance back in service
  4. Verify health
  5. Move to the next instance
- **Implementation**:
  ```yaml
  jobs:
    rolling_deploy:
      runs-on: ubuntu-latest
      steps:
        - uses: actions/checkout@v3
        - name: Get instance list
          id: instances
          run: echo "instances=$(./get_instances.sh)" >> $GITHUB_OUTPUT
        - name: Deploy to each instance
          run: |
            for instance in ${{ steps.instances.outputs.instances }}; do
              ./deploy_to_instance.sh $instance
              ./verify_instance.sh $instance
            done
  ```

## Deployment Workflow

Our standard deployment workflow follows these steps:

1. **Build**: Create deployment artifacts
2. **Test**: Run pre-deployment tests
3. **Deploy**: Deploy to target environment
4. **Verify**: Run post-deployment tests
5. **Monitor**: Watch for issues after deployment

```yaml
name: Deploy API

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

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Set up environment
        uses: actions/setup-node@v3
        with:
          node-version: '16'
      - name: Install dependencies
        run: npm ci
      - name: Build
        run: npm run build
      - name: Upload build artifacts
        uses: actions/upload-artifact@v3
        with:
          name: build-artifacts
          path: dist/

  test:
    needs: build
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Set up environment
        uses: actions/setup-node@v3
        with:
          node-version: '16'
      - name: Download build artifacts
        uses: actions/download-artifact@v3
        with:
          name: build-artifacts
          path: dist/
      - name: Run tests
        run: npm test

  deploy:
    needs: test
    runs-on: ubuntu-latest
    environment: ${{ github.event.inputs.environment }}
    steps:
      - uses: actions/checkout@v3
      - name: Download build artifacts
        uses: actions/download-artifact@v3
        with:
          name: build-artifacts
          path: dist/
      - name: Deploy to ${{ github.event.inputs.environment }}
        run: |
          echo "Deploying to ${{ github.event.inputs.environment }}"
          # Deployment commands specific to environment
      - name: Verify deployment
        run: |
          echo "Verifying deployment"
          # Verification commands
```

## Environment Configuration Management

We manage environment-specific configuration using GitHub Environments:

1. **Environment Secrets**: Store sensitive values
2. **Environment Variables**: Store non-sensitive configuration
3. **Protection Rules**: Enforce approval requirements
4. **Deployment Branches**: Restrict which branches can deploy

```yaml
jobs:
  deploy:
    runs-on: ubuntu-latest
    environment:
      name: production
      url: https://api.example.com
    steps:
      - uses: actions/checkout@v3
      - name: Deploy with secrets
        env:
          API_KEY: ${{ secrets.API_KEY }}
          DATABASE_URL: ${{ secrets.DATABASE_URL }}
        run: ./deploy.sh
```

## Rollback Strategy

Our rollback strategy ensures quick recovery from failed deployments:

1. **Automated Rollbacks**: Automatically roll back on failed smoke tests
2. **Manual Rollbacks**: Provide workflow for manual rollback
3. **Version Tracking**: Maintain deployment history for rollback targets

```yaml
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Record current version
        run: |
          CURRENT_VERSION=$(curl -s https://api.example.com/version)
          echo "CURRENT_VERSION=$CURRENT_VERSION" >> $GITHUB_ENV
      - name: Deploy new version
        run: ./deploy.sh
      - name: Run smoke tests
        id: smoke_tests
        run: ./smoke_tests.sh
      - name: Rollback on failure
        if: failure() && steps.smoke_tests.outcome == 'failure'
        run: |
          echo "Smoke tests failed, rolling back to ${{ env.CURRENT_VERSION }}"
          ./rollback.sh ${{ env.CURRENT_VERSION }}
```

## Database Migrations

Our deployment pipeline handles database migrations carefully:

1. **Migration Scripts**: Version-controlled migration scripts
2. **Pre-Deployment Migrations**: Run migrations before code deployment
3. **Rollback Scripts**: Provide rollback scripts for each migration
4. **Validation**: Verify database state after migration

```yaml
jobs:
  migrate_database:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Set up database tools
        run: npm install -g db-migrate
      - name: Backup database
        run: ./backup_db.sh
      - name: Run migrations
        run: db-migrate up
      - name: Verify migrations
        run: ./verify_db.sh
```

## Conclusion

This deployment pipeline provides a robust, flexible approach to deploying web APIs across multiple environments. By leveraging GitHub Actions and implementing these deployment strategies, we can ensure reliable, consistent deployments with minimal downtime and risk.
