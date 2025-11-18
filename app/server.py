from fastapi import FastAPI
from pydantic import BaseModel
import os
from dotenv import load_dotenv
from google.adk.cli.fast_api import get_fast_api_app

# Load environment variables
load_dotenv()

AGENT_DIR = os.path.dirname(os.path.abspath(__file__))
app_args = {"agents_dir": AGENT_DIR, "web": True}

# Create FastAPI app with ADK integration
app: FastAPI = get_fast_api_app(**app_args)

class AgentRequest(BaseModel):
    message: str
    image_base64: str | None = None
    filename: str | None = None

@app.post("/agent")
async def run_agent(payload: AgentRequest):
    enriched = payload.message

    if payload.image_base64:
        enriched += f"\n\n[IMAGE_BASE64_START]\n{payload.image_base64}\n[IMAGE_BASE64_END]"

    result = runtime.run(enriched)

    return {
        "response": result.final_response,
        "steps": result.steps,
    }

@app.get("/")
async def home():
    return {"status": "HealthSense Agent is running"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080, log_level="info")
