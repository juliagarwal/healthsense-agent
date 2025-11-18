from google.cloud import firestore
import time

def save_record(record: dict):
    db = firestore.Client()
    record["timestamp"] = time.time()

    db.collection("health_records").add(record)

    return {"status": "saved"}
