#output "public_ip_address" {
#  value = azurerm_public_ip.example.ip_address
#}

data "azurerm_public_ip" "example-vm-ip" {
  name                = "example-vm-ip"
  resource_group_name = "example-resource-group-tenant"
}

output "public_ip_address" {
  value = data.azurerm_public_ip.example-vm-ip.ip_address
}

