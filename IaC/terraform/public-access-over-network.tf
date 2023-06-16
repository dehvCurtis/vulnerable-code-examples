
    # OWASP Top 10 2021 Category A1 - Broken Access Control
    # AWS Documentation - Amazon EC2 instance IP addressing
    # AWS Documentation - Public and private replication instances
    # AWS Documentation - VPC Peering
    # MITRE, CWE-284 - Improper Access Control
    # MITRE, CWE-668 - Exposure of Resource to Wrong Sphere
    # OWASP Top 10 2017 Category A5 - Broken Access Control

# For AWS:
resource "aws_instance" "example" {
  associate_public_ip_address = true # Sensitive
}
resource "aws_dms_replication_instance" "example" {
  publicly_accessible = true # Sensitive
}

# For Azure:
resource "azurerm_postgresql_server" "example"  {
  public_network_access_enabled = true # Sensitive
}
resource "azurerm_postgresql_server" "example"  {
  public_network_access_enabled = true # Sensitive
}
resource "azurerm_kubernetes_cluster" "production" {
  api_server_authorized_ip_ranges = ["176.0.0.0/4"] # Sensitive
  default_node_pool {
    enable_node_public_ip = true # Sensitive
  }
}

# For GCP:
resource "google_compute_instance" "example" {
  network_interface {
    network = "default"

    access_config {  # Sensitive
      # Ephemeral public IP
    }
  }
