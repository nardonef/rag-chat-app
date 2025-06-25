output "cloud_run_url" {
  value = google_cloud_run_service.fantasy-rag.status[0].url
}
