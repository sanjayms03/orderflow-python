# OrderFlow Python — SkyForge AI Test Fixture

> **WARNING: Intentionally vulnerable test fixture for SkyForge AI. Do not deploy. Keep the repository private.**

OrderFlow is a demo e-commerce order-processing platform intended to exercise code security, dependency scanning,
Terraform cost analysis, test generation, and code-health checks. It uses fake credentials and example-only URLs.
No cloud resources are created by these files.

## Components
- Customer, product, order, payment, inventory and reporting APIs
- Order-event worker and Lambda-style handlers
- Terraform examples for VPC, NAT gateways, EC2, RDS, S3, EBS, ALB, Lambda, SQS and IAM
- Deliberately thin tests and `EXPECTED_FINDINGS.md` as a validation answer key
- Intentionally insecure Docker/CI examples for static analysis

## Local setup
```bash
python3.11 -m venv .venv && source .venv/bin/activate && pip install -e '.[test]'
python scripts/run_local.py
```

## Tests
```bash
pytest --cov=orderflow --cov-report=term && behave functional-tests/features
```

## Safety
- Do not run `terraform apply`.
- Do not put real credentials in `.env` or CI settings.
- Bind local development servers to `127.0.0.1`.
- Keep this fixture in a private repository; do not use it as a production template.

## SkyForge
Add the repository through SkyForge's service onboarding flow, run a full scan, and compare results with
`EXPECTED_FINDINGS.md`. Dependency advisories can change over time; validate pinned versions with OSV or your
organization-approved vulnerability database.
