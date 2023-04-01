terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 2.0"
    }
  }

  required_version = ">= 1.2.0"
}

provider "azurerm" {
  features {}
}

variable "docker_image" {
  type    = string
  default = "alpine"
}

resource "azurerm_resource_group" "example" {
  name     = "example-resource-group-tenant"
  location = "eastus2"
}


resource "azurerm_virtual_machine" "example" {
  name                  = "example-vm-3"
  location              = azurerm_resource_group.example.location
  resource_group_name   = azurerm_resource_group.example.name
  network_interface_ids = ["/subscriptions/b769a559-e8c9-4236-a79b-40c2a654a68c/resourceGroups/example-resource-group-tenant/providers/Microsoft.Network/networkInterfaces/example-vm567"]
  vm_size               = "Standard_B2s"

#  custom_data = filebase64("customdata.tpl")

  storage_image_reference {
    publisher = "Canonical"
    offer     = "UbuntuServer"
    sku       = "18.04-LTS"
    version   = "latest"
  }

  storage_os_disk {
    name              = "example-vm-3"
    caching           = "ReadWrite"
    create_option     = "FromImage"
    managed_disk_type = "Standard_LRS"
  }

  os_profile {
    computer_name  = "example"
    admin_username = "azureuser"
    admin_password = "@Password@123"
 custom_data = base64encode(file("customdata.tpl"))
#	custom_data=<<EOF
#                #!/bin/bash
#                sudo apt-get update
#                sudo apt-get install -y docker.io
#                sudo chmod 777 /var/run/docker.sock
#                docker pull ${var.docker_image}
#                docker run -d --rm --name web-test -p 80:8000 ${var.docker_image}
#                EOF
  }

  os_profile_linux_config {
    disable_password_authentication = false
  }

#  custom_data=<<EOF
#		#!/bin/bash
#		sudo apt-get update
#		sudo apt-get install -y docker.io
#		sudo chmod 777 /var/run/docker.sock
#		docker pull ${var.docker_image}
#		docker run -d --rm --name web-test -p 80:8000 ${var.docker_image}
#		EOF
  # provisioner "remote-exec" {
     #inline = [
     #  "sudo apt-get update",
     #  "sudo apt-get install -y docker.io",
     #  "sudo chmod 777 /var/run/docker.sock",
     #  #"sudo usermod -aG docker ${var.admin_username}",
     #  #"sudo chmod 777 /var/run/docker.sock",
    #   "docker pull ${var.docker_image}",
    #   "docker run -d --rm --name web-test -p 80:8000 ${var.docker_image}"
   #  ]
   #}
  
}
