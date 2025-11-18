import base64
import uuid
from google.cloud import storage

def upload_to_gcs(file_base64: str, filename: str):
    client = storage.Client()
    bucket = client.bucket("healthsense-prescriptions")

    blob_name = f"{uuid.uuid4()}_{filename}"
    blob = bucket.blob(blob_name)

    file_bytes = base64.b64decode(file_base64)
    blob.upload_from_string(file_bytes, content_type="image/jpeg")

    blob.make_public()

    return {"gcs_url": blob.public_url}

