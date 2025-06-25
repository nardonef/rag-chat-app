provider "google" {
  project = var.project_id
  region  = var.region
}

resource "google_artifact_registry_repository" "app_repo" {
  name     = var.repo_name
  repository_id = "rag-chat-app"
  format   = "DOCKER"
  location = var.region
}

resource "google_cloud_run_service" "fantasy-rag" {
  name     = "fantasy-rag"
  location = var.region

  template {
    spec {
      containers {
        image = var.image_url
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
  member   = "allUsers"
}
