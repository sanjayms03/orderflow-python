resource "aws_instance" "api_a" { ami = "ami-0123456789abcdef0"
  instance_type = "m5.4xlarge"
  subnet_id = aws_subnet.a.id
  vpc_security_group_ids = [aws_security_group.open.id]
  associate_public_ip_address = true
  monitoring = false
  root_block_device { volume_type = "gp2"
  volume_size = 500
  encrypted = false }
  tags = { Name = "orderflow-api-a", Project = "orderflow", Owner = "skyforge-test-fixture" } }
resource "aws_instance" "api_b" { ami = "ami-0123456789abcdef0"
  instance_type = "c5.9xlarge"
  subnet_id = aws_subnet.b.id
  vpc_security_group_ids = [aws_security_group.open.id]
  associate_public_ip_address = true
  monitoring = false
  root_block_device { volume_type = "gp2"
  volume_size = 500
  encrypted = false }
  tags = { Name = "orderflow-api-b", Project = "orderflow", Owner = "skyforge-test-fixture" } }
resource "aws_instance" "worker" { ami = "ami-0123456789abcdef0"
  instance_type = "r5.8xlarge"
  subnet_id = aws_subnet.c.id
  vpc_security_group_ids = [aws_security_group.open.id]
  associate_public_ip_address = true
  monitoring = false
  root_block_device { volume_type = "gp2"
  volume_size = 500
  encrypted = false }
  tags = { Name = "orderflow-worker", Project = "orderflow", Owner = "skyforge-test-fixture" } }
resource "aws_instance" "report_a" { ami = "ami-0123456789abcdef0"
  instance_type = "m5.2xlarge"
  subnet_id = aws_subnet.a.id
  vpc_security_group_ids = [aws_security_group.open.id]
  associate_public_ip_address = true
  monitoring = false
  root_block_device { volume_type = "gp2"
  volume_size = 500
  encrypted = false }
  tags = { Name = "orderflow-report-a", Project = "orderflow", Owner = "skyforge-test-fixture" } }
resource "aws_instance" "report_b" { ami = "ami-0123456789abcdef0"
  instance_type = "m5.2xlarge"
  subnet_id = aws_subnet.b.id
  vpc_security_group_ids = [aws_security_group.open.id]
  associate_public_ip_address = true
  monitoring = false
  root_block_device { volume_type = "gp2"
  volume_size = 500
  encrypted = false }
  tags = { Name = "orderflow-report-b", Project = "orderflow", Owner = "skyforge-test-fixture" } }
resource "aws_instance" "bastion" { ami = "ami-0123456789abcdef0"
  instance_type = "t3.2xlarge"
  subnet_id = aws_subnet.c.id
  vpc_security_group_ids = [aws_security_group.open.id]
  associate_public_ip_address = true
  monitoring = false
  root_block_device { volume_type = "gp2"
  volume_size = 500
  encrypted = false }
  tags = { Name = "orderflow-bastion", Project = "orderflow", Owner = "skyforge-test-fixture" } }
