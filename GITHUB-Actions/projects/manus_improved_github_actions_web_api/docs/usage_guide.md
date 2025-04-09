# GitHub Actions Web API Automation Usage Guide

This guide provides step-by-step instructions for using the GitHub Actions workflows to automate your web API development, testing, deployment, and monitoring processes.

## Table of Contents

1. [Getting Started](#getting-started)
2. [Setting Up Your Repository](#setting-up-your-repository)
3. [Continuous Integration](#continuous-integration)
4. [Continuous Deployment](#continuous-deployment)
5. [Monitoring and Health Checks](#monitoring-and-health-checks)
6. [Using Advanced Features](#using-advanced-features)
7. [Customization Guide](#customization-guide)
8. [FAQ](#faq)

## Getting Started

### Prerequisites

Before using these GitHub Actions workflows, ensure you have:

- A GitHub account
- A web API project (Node.js/Express example provided)
- Basic understanding of GitHub Actions
- Repository permissions to create workflows

### Quick Start

1. Copy the `.github` directory to your repository
2. Modify the workflows to match your project structure
3. Push the changes to your repository
4. Navigate to the Actions tab to see your workflows

## Setting Up Your Repository

### Directory Structure

Ensure your repository follows a similar structure:

```
your-api-project/
├── src/                          # API source code
├── tests/                        # Test files
├── .github/
│   ├── workflows/                # GitHub Actions workflow files
│   └── actions/                  # Custom composite actions
├── package.json                  # Project dependencies and scripts
└── .env.example                  # Environment variables template
```

### Environment Setup

1. **Create Environment Secrets**

   Go to your repository settings → Secrets and variables → Actions → New repository secret

   Required secrets:
   - `MONGO_URI`: MongoDB connection string
   - `JWT_SECRET`: Secret for JWT token generation
   - `API_URL`: URL of your deployed API (for monitoring)

2. **Configure Environments**

   Go to your repository settings → Environments → New environment

   Create environments for:
   - `development`
   - `staging`
   - `production`

   For production, add protection rules:
   - Required reviewers
   - Wait timer (e.g., 10 minutes)

3. **Branch Protection**

   Go to your repository settings → Branches → Add rule

   Protect your main branch:
   - Require pull request reviews
   - Require status checks to pass
   - Require branches to be up to date

## Continuous Integration

The CI workflow automatically tests your code when changes are pushed or pull requests are created.

### Running CI Workflow

The CI workflow runs automatically on:
- Push to main and develop branches
- Pull requests to main and develop branches

You can also run it manually:
1. Go to Actions tab
2. Select "CI Pipeline"
3. Click "Run workflow"
4. Select the branch
5. Click "Run workflow"

### CI Workflow Steps

1. **Linting**: Checks code style and quality
2. **Testing**: Runs unit and integration tests
3. **Building**: Creates a build artifact

### Viewing CI Results

1. Go to Actions tab
2. Find the latest CI workflow run
3. Click on it to see details
4. View job outputs and logs
5. Download artifacts if needed

### Customizing CI

To customize the CI workflow:

1. Edit `.github/workflows/ci.yml`
2. Modify the triggers to match your branch structure:
   ```yaml
   on:
     push:
       branches: [ main, develop, your-branch ]
   ```
3. Adjust the Node.js version:
   ```yaml
   - name: Setup Node.js
     uses: actions/setup-node@v3
     with:
       node-version: '18'  # Change to your version
   ```
4. Add or remove steps as needed

## Continuous Deployment

The CD workflow automates deploying your API to different environments.

### Running CD Workflow

The CD workflow runs automatically on:
- Push to main branch (deploys to development)

For manual deployment:
1. Go to Actions tab
2. Select "CD Pipeline"
3. Click "Run workflow"
4. Select the branch
5. Choose the environment (development, staging, production)
6. Click "Run workflow"

### CD Workflow Steps

1. **Prepare**: Creates deployment package
2. **Deploy**: Deploys to the selected environment
3. **Verify**: Runs post-deployment checks

### Deployment Environments

- **Development**: Automatic deployment, minimal restrictions
- **Staging**: Manual deployment, testing environment
- **Production**: Manual deployment, requires approval

### Customizing CD

To customize the CD workflow:

1. Edit `.github/workflows/cd.yml`
2. Modify the deployment steps for your hosting platform:
   ```yaml
   - name: Deploy to server
     run: |
       # Replace with your deployment commands
       scp -r deploy/* user@your-server:/path/to/api
       ssh user@your-server "cd /path/to/api && npm install && pm2 restart api"
   ```
3. Adjust environment-specific configurations

## Monitoring and Health Checks

The monitoring workflow regularly checks your API's health and performance.

### Running Monitoring Workflow

The monitoring workflow runs automatically:
- Every 15 minutes (scheduled)

For manual monitoring:
1. Go to Actions tab
2. Select "Monitoring"
3. Click "Run workflow"
4. Click "Run workflow"

### Monitoring Workflow Steps

1. **Health Check**: Verifies API availability
2. **Performance Check**: Measures response times
3. **Security Scan**: Checks for vulnerabilities (weekly)

### Customizing Monitoring

To customize the monitoring workflow:

1. Edit `.github/workflows/monitoring.yml`
2. Adjust the schedule:
   ```yaml
   on:
     schedule:
       - cron: '*/30 * * * *'  # Every 30 minutes
   ```
3. Modify the health check endpoints:
   ```yaml
   - name: Check API health endpoint
     run: |
       API_URL="${{ secrets.API_URL }}/your-health-endpoint"
   ```
4. Configure notification channels

## Using Advanced Features

### Matrix Testing

Matrix testing allows testing across multiple configurations:

1. Edit the CI workflow
2. Configure the matrix strategy:
   ```yaml
   strategy:
     matrix:
       node-version: [14.x, 16.x, 18.x]
       os: [ubuntu-latest, windows-latest]
   ```
3. Use matrix variables in steps:
   ```yaml
   - name: Setup Node.js ${{ matrix.node-version }}
     uses: actions/setup-node@v3
     with:
       node-version: ${{ matrix.node-version }}
   ```

### Database Migrations

To run database migrations:

1. Go to Actions tab
2. Select "Database Migrations"
3. Click "Run workflow"
4. Select the environment
5. Click "Run workflow"

### API Documentation Generation

To generate API documentation:

1. Go to Actions tab
2. Select "API Documentation Generation"
3. Click "Run workflow"
4. Click "Run workflow"

The documentation will be generated and deployed to GitHub Pages.

### Dependency Management

To update dependencies:

1. Go to Actions tab
2. Select "Dependency Management"
3. Click "Run workflow"
4. Choose update type (patch, minor, major)
5. Click "Run workflow"

A pull request will be created with the updates.

## Customization Guide

### Adding New Workflows

To add a new workflow:

1. Create a new YAML file in `.github/workflows/`
2. Define the workflow structure:
   ```yaml
   name: My New Workflow

   on:
     workflow_dispatch:  # Manual trigger

   jobs:
     my_job:
       runs-on: ubuntu-latest
       steps:
         - name: Checkout code
           uses: actions/checkout@v3
         
         # Add your steps here
   ```
3. Commit and push the file

### Creating Custom Actions

To create a custom composite action:

1. Create a directory in `.github/actions/my-action/`
2. Create an `action.yml` file:
   ```yaml
   name: 'My Custom Action'
   description: 'Description of what your action does'
   inputs:
     my-input:
       description: 'Input description'
       required: false
       default: 'default value'
   
   runs:
     using: "composite"
     steps:
       - name: My step
         shell: bash
         run: echo "Hello ${{ inputs.my-input }}"
   ```
3. Use your action in workflows:
   ```yaml
   - name: Use my custom action
     uses: ./.github/actions/my-action
     with:
       my-input: 'world'
   ```

### Workflow Optimization

To optimize your workflows:

1. **Use Caching**:
   ```yaml
   - name: Cache dependencies
     uses: actions/cache@v3
     with:
       path: node_modules
       key: ${{ runner.os }}-node-${{ hashFiles('**/package-lock.json') }}
   ```

2. **Conditional Execution**:
   ```yaml
   - name: Run only on main branch
     if: github.ref == 'refs/heads/main'
     run: echo "This runs only on main branch"
   ```

3. **Path Filtering**:
   ```yaml
   on:
     push:
       paths:
         - 'src/**'
         - 'package.json'
   ```

## FAQ

### How do I debug a failing workflow?

1. Check the workflow run logs in the Actions tab
2. Enable debug logging by setting the secret `ACTIONS_RUNNER_DEBUG` to `true`
3. Add debug steps to print environment information:
   ```yaml
   - name: Debug info
     run: |
       echo "Working directory: $(pwd)"
       echo "Environment: ${{ toJSON(env) }}"
   ```

### How do I skip CI for minor changes?

Add `[skip ci]` or `[ci skip]` to your commit message:
```
git commit -m "Update README.md [skip ci]"
```

### How do I add a new environment?

1. Go to repository settings → Environments → New environment
2. Name your environment (e.g., `qa`)
3. Configure protection rules if needed
4. Add environment secrets
5. Update the CD workflow to include the new environment:
   ```yaml
   inputs:
     environment:
       description: 'Environment to deploy to'
       type: choice
       options:
         - development
         - staging
         - production
         - qa  # Add your new environment
   ```

### How do I trigger a workflow from another repository?

Use the `repository_dispatch` event:

1. Create a personal access token with `repo` scope
2. Add it as a secret in the source repository
3. Use a curl command to trigger the workflow:
   ```yaml
   - name: Trigger workflow in another repo
     run: |
       curl -X POST \
         -H "Authorization: token ${{ secrets.PAT_TOKEN }}" \
         -H "Accept: application/vnd.github.v3+json" \
         https://api.github.com/repos/owner/repo/dispatches \
         -d '{"event_type":"my-event"}'
   ```
4. Configure the target workflow to listen for the event:
   ```yaml
   on:
     repository_dispatch:
       types: [my-event]
   ```

### How do I secure sensitive information?

1. Never hardcode secrets in workflow files
2. Use repository or environment secrets
3. Limit secret access to specific environments
4. Use OIDC for cloud provider authentication
5. Regularly rotate secrets
