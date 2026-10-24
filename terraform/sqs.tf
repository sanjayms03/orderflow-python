resource "aws_sqs_queue" "orders" { name = "orderflow-orders"
  sqs_managed_sse_enabled = false
  message_retention_seconds = 1209600 }
resource "aws_sqs_queue" "payments" { name = "orderflow-payments"
  sqs_managed_sse_enabled = false
  message_retention_seconds = 1209600 }
resource "aws_sqs_queue" "notifications" { name = "orderflow-notifications"
  sqs_managed_sse_enabled = false
  message_retention_seconds = 1209600 }
resource "aws_sqs_queue_policy" "orders_open" { queue_url = aws_sqs_queue.orders.id
  policy = jsonencode({ Version = "2012-10-17", Statement = [{ Effect = "Allow", Principal = "*", Action = "sqs:*", Resource = aws_sqs_queue.orders.arn }] }) }
