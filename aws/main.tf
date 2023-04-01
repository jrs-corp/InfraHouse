terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.16"
    }
  }

  required_version = ">= 1.2.0"
}

variable "docker_image" {
  type	= string
  default = "alpine"
}

provider "aws" {
  region  = "us-east-1"
}

resource "aws_key_pair" "terraform_ec2_key" {
  key_name = "terraform_ec2_key"
  public_key = "${file("terraform_ec2_key.pub")}"
  
}

#resource "aws_security_group_rule" "web_server_inbound_rule" {
#  type        = "ingress"
#  from_port   = 80
#  to_port     = 80
#  protocol    = "tcp"
#  cidr_blocks = ["0.0.0.0/0"]
#  security_group_id = "sg-0411ef64de1597708"
#}

#resource "aws_security_group_rule" "ssh_inbound_rule" {
#  type        = "ingress"
#  from_port   = 23
#  to_port     = 23
#  protocol    = "tcp"
#  cidr_blocks = ["0.0.0.0/0"]
#  security_group_id = "sg-0411ef64de1597708"
#}

resource "aws_instance" "app_server" {
  ami           = "ami-0b5eea76982371e91"
  instance_type = "t2.micro"
  key_name = aws_key_pair.terraform_ec2_key.key_name
  # Add username and password for login
  #connection {
  #  type        = "ssh"
  #  user        = "ec2-user"
  #  password    = "password"
  #  host        = self.public_ip
  #  timeout     = "2m"
  #}

  tags = {
    Name = var.instance_name
  }

  #user_data = <<-EOF
  #            #!/bin/bash
  #            sudo yum install docker -y
#	      sudo systemctl start docker
#	      sudo chmod 777 /var/run/docker.sock
#	      docker pyll python
#	      docker run python
#	      docker pull ${var.docker_image}
 #             #docker pull crccheck/hello-world
 #             docker run -d --rm --name web-test -p 80:8000 ${var.docker_image}
 #             EOF
#
}



