provider "google" {
 credentials = file("CREDENTIALS_FILE.json")
 project     = var.project
 region      = substr(var.zone, 0, -2)
}
