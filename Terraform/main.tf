provider "aws" {
  region = "ap-south-1"
}

resource "aws_instance" "example" {
  ami           = "ami-06b72b3b2a773be2b"
  instance_type = "t2.micro"

  tags = {
    Name = "terraform-example"
  }
}
