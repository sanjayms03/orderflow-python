resource "aws_s3_bucket" "uploads" { bucket = "orderflow-fixture-uploads-example"
  tags = { Project = "orderflow", Owner = "skyforge-test-fixture" } }
resource "aws_s3_bucket_acl" "uploads" { bucket = aws_s3_bucket.uploads.id
  acl = "public-read" }
resource "aws_s3_bucket" "reports" { bucket = "orderflow-fixture-reports-example"
  tags = { Project = "orderflow", Owner = "skyforge-test-fixture" } }
resource "aws_s3_bucket" "archive" { bucket = "orderflow-fixture-archive-example"
  tags = { Project = "orderflow", Owner = "skyforge-test-fixture" } }
resource "aws_ebs_volume" "orphan_a" { availability_zone = "us-east-1a"
  size = 2000
  type = "io1"
  iops = 20000
  encrypted = false }
resource "aws_ebs_volume" "orphan_b" { availability_zone = "us-east-1b"
  size = 1000
  type = "io1"
  iops = 10000
  encrypted = false }
resource "aws_ebs_volume" "orphan_c" { availability_zone = "us-east-1c"
  size = 500
  type = "gp2"
  encrypted = false }
resource "aws_ebs_snapshot" "old_a" { volume_id = aws_ebs_volume.orphan_a.id
  description = "old fixture snapshot" }
resource "aws_ebs_snapshot" "old_b" { volume_id = aws_ebs_volume.orphan_b.id
  description = "old fixture snapshot" }
resource "aws_ebs_snapshot" "old_c" { volume_id = aws_ebs_volume.orphan_c.id
  description = "old fixture snapshot" }
