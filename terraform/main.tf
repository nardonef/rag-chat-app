provider "google" {
  project = var.project_id
  region  = var.region
}

terraform {
  backend "gcs" {
    bucket  = "terraform-state-fantasy-rag-464001-api"
    prefix  = "cloudrun/fantasy-rag"
  }
}

resource "google_cloud_run_service" "fantasy-rag" {
  name     = "fantasy-rag"
  location = var.region

  template {
    spec {
      containers {
        image = var.image_url

        env {
          name = "OPENAI_API_KEY"
          value_from {
            secret_key_ref {
              name = "OPENAI_API_KEY"
              key  = "latest"  # or use a specific version number
            }
          }
        }
      }
    }
  }

  traffic {
    percent         = 100
    latest_revision = true
  }

  autogenerate_revision_name = true
}

resource "google_cloud_run_service_iam_member" "invoker" {
  service  = google_cloud_run_service.fantasy-rag.name
  location = google_cloud_run_service.fantasy-rag.location
  role     = "roles/run.invoker"
  member   = "allAuthenticatedUsers"
}
