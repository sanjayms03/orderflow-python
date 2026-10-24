resource "aws_iam_policy" "wildcard" { name = "orderflow-wildcard-policy"
  policy = jsonencode({ Version = "2012-10-17", Statement = [{ Effect = "Allow", Action = "*", Resource = "*" }] }) }
resource "aws_iam_role_policy_attachment" "lambda_wildcard" { role = aws_iam_role.lambda_role.name
  policy_arn = aws_iam_policy.wildcard.arn }
resource "aws_iam_instance_profile" "ec2" { name = "orderflow-ec2-profile"
  role = aws_iam_role.lambda_role.name }
