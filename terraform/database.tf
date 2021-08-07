resource "google_sql_database_instance" "master" {
  name             = var.project
  database_version = "POSTGRES_11"


  settings {
    tier = "db-f1-micro"
    ip_configuration {
      ipv4_enabled    = true
      private_network = google_compute_network.vpc.id
      require_ssl = true
      authorized_networks {
        value = "34.116.141.114"
      }
      authorized_networks {
        value = "34.116.252.131"
      }
    }
  }
}

resource "google_sql_ssl_cert" "client_cert" {
  common_name = "client-ssl"
  instance    = google_sql_database_instance.master.name
}