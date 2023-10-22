# Define the required providers
provider "google" {
  project = "tough-flow-388709"
  region  = "us-east1"
}

# Create a GCS bucket
resource "google_storage_bucket" "iss_data_bucket" {
  name     = "iss_data"
  location = "us-east1"

  # Set the roles and permissions for the bucket
  uniform_bucket_level_access = true
}

# Create a Pub/Sub topic
resource "google_pubsub_topic" "gcs_trigger_topic" {
  name = "gcs-trigger-topic"
}

# Grant roles to the service account for GCS bucket
resource "google_project_iam_binding" "gcs_iam_binding" {
  project = "tough-flow-388709"
  role    = "roles/storage.admin"
  members = ["serviceAccount:test_sa@tough-flow-388709.iam.gserviceaccount.com"]
}

# Grant roles to the service account for Pub/Sub topic
resource "google_project_iam_binding" "pubsub_iam_binding" {
  project = "tough-flow-388709"
  role    = "roles/pubsub.admin"
  members = ["serviceAccount:test_sa@tough-flow-388709.iam.gserviceaccount.com"]
}

# Create a notification for the GCS bucket
resource "google_storage_notification" "gcs_trigger" {
  bucket = google_storage_bucket.iss_data_bucket.name

  topic = google_pubsub_topic.gcs_trigger_topic.name

  payload_format = "JSON_API_V1"

  event_types = ["OBJECT_FINALIZE"]
}

