output "vpc_id" { value = aws_vpc.main.id }
output "primary_db_endpoint" { value = aws_db_instance.primary.address }
