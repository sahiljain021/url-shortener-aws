provider "aws" {
  region = "ap-south-1"
}

resource "aws_dynamodb_table" "url_shortener" {
  name         = "url-shortener"
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "short_code"

  attribute {
    name = "short_code"
    type = "S"
  }

  ttl {
    attribute_name = "expires_at"
    enabled        = true
  }

  tags = { Name = "url-shortener" }
}