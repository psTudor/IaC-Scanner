resource "azurerm_storage_account" "insecure_storage" {
  name                     = "mystorageacc"
  resource_group_name      = "my-rg"
  location                 = "West Europe"
  account_tier             = "Standard"
  account_replication_type = "GRS"

  enable_https_traffic_only = false
  allow_nested_items_to_be_public = true
}

resource "azurerm_storage_account" "secure_storage" {
  name                     = "mystorageacc2"
  resource_group_name      = "my-rg"
  location                 = "West Europe"
  account_tier             = "Standard"
  account_replication_type = "LRS"

  enable_https_traffic_only = true
  allow_nested_items_to_be_public = false
}