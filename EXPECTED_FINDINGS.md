# Expected Findings — Python

> Fixture answer key. Findings are intentional. Do not deploy.

## Dependency risks
`pyproject.toml` pins old Flask/Werkzeug/Jinja2/requests/urllib3/PyJWT/cryptography/paramiko/gunicorn/boto3/botocore versions.
Verify exact package/version advisory matches against OSV or your approved scanner; advisories and aliases evolve.

## Application security
- `main/orderflow/repositories/customer_repo.py`: f-string SQL query (SQL injection).
- `main/orderflow/api/admin.py`: `eval` and `shell=True` command construction.
- `main/orderflow/services/report_service.py`: untrusted template source (SSTI risk).
- `main/orderflow/integrations/payment_gateway.py`: TLS verification disabled; no request timeout.
- `main/orderflow/integrations/shipping_client.py`: caller-controlled URL (SSRF pattern).
- `main/orderflow/utils/serialization.py`: unsafe `pickle.loads`.
- `main/orderflow/auth/jwt_auth.py`: signature verification disabled; static secret.
- `main/orderflow/auth/passwords.py`: MD5 and non-cryptographic `random`.
- `main/orderflow/utils/files.py`: `tempfile.mktemp`, permissive `chmod(777)`, unsafe path handling.
- `main/orderflow/api/uploads.py`: user-supplied filename path composition.
- `main/orderflow/api/orders.py`: exception detail leakage.
- `main/orderflow/integrations/s3_storage.py`: public-read ACL.
- `.github/workflows/ci.yml`: broad permissions, pull_request_target, unpinned actions, secret echoed.
- `Dockerfile`: latest base, root user, remote ADD, secret ENV.

## Terraform security/cost
- `terraform/network.tf`: SSH/Postgres/all TCP ports open to the world.
- `terraform/compute.tf`: six large instances, public IPs, gp2 500GB disks, encryption disabled, monitoring off.
- `terraform/database.tf`: two large publicly accessible unencrypted databases; large io1 provisioned IOPS; deletion protection off.
- `terraform/storage.tf`: public-read S3 ACL, no lifecycle/encryption/versioning controls; unattached expensive EBS volumes and old snapshots.
- `terraform/network.tf`: three NAT gateways and three EIPs; assess consolidation.
- `terraform/lambda.tf`: 10GB memory, 15-minute timeout, old runtime, x86_64, plaintext fake token.
- `terraform/sqs.tf`: unencrypted queues, no DLQ, long retention, wildcard queue policy.
- `terraform/loadbalancer.tf`: idle ALB.
- `terraform/iam.tf`: wildcard action/resource policy.
- Cost remediation directions: rightsize, gp2→gp3, Graviton where compatible, consolidate NAT, remove idle ALB and unattached storage, set S3 lifecycle, reduce provisioned RDS IOPS.

## Quality and tests
- Duplicated domain aggregation logic under `main/orderflow/services/`.
- Low test coverage by design; tests focus only on money, validators, dates and 3 API happy paths.
- Expected coverage is intentionally low; exact percentage depends on tool and import collection.
