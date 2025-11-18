from google.adk.types import Tool

from .gcs_tool import upload_to_gcs
from .vision_tool import extract_prescription_data
from .advice_tool import generate_health_advice
from .firebase_tool import save_record

upload_to_gcs_tool = Tool(
    name="upload_to_gcs",
    description="Uploads a prescription image to GCS.",
    input_schema={
        "type": "object",
        "properties": {
            "file_base64": {"type": "string"},
            "filename": {"type": "string"},
        },
        "required": ["file_base64", "filename"]
    },
    func=upload_to_gcs
)

extract_prescription_tool = Tool(
    name="extract_prescription_data",
    description="Extracts medicine info from an uploaded prescription",
    input_schema={
        "type": "object",
        "properties": {
            "gcs_url": {"type": "string"}
        },
        "required": ["gcs_url"]
    },
    func=extract_prescription_data
)

generate_health_tool = Tool(
    name="generate_health_advice",
    description="Generate friendly health suggestions",
    input_schema={
        "type": "object",
        "properties": {
            "extracted_json": {"type": "string"}
        },
        "required": ["extracted_json"]
    },
    func=generate_health_advice
)

save_record_tool = Tool(
    name="save_record",
    description="Store record in Firestore",
    input_schema={
        "type": "object",
        "properties": {
            "record": {"type": "object"}
        },
        "required": ["record"]
    },
    func=save_record
)

TOOLS = [
    upload_to_gcs_tool,
    extract_prescription_tool,
    generate_health_tool,
    save_record_tool
]
