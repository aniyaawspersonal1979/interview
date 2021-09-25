provider "aws" {
	region = "us-east-1"

}

resource "aws_s3_bucket" "b-qa" {
  bucket = "qa-interview-123"
  acl    = "private"

  tags = {
    Name        = "qa-interview"
    Environment = "qa"
  }
}

resource "aws_s3_bucket" "b-dev" {
  bucket = "dev-interview-123"
  acl    = "private"

  tags = {
    Name        = "dev-interview"
    Environment = "dev"
  }
}
