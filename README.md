# HealthSense — AI Preventive Health Agent

A compact prototype AI agent that analyses prescriptions and basic health inputs to produce preventive insights and human-readable summaries. Built with Google’s Agent Developer Kit (ADK) and a Gemini-capable LLM, with a lightweight FastAPI backend.

---

## What it does
- Parse prescription text or simple report uploads.
- Extract medicines, dosages and basic red-flags.
- Produce an AI-generated executive summary and a short CID (STAR) style note.
- Return a basic, non-diagnostic risk score from an internal model.

---

## Tech stack
- Backend: FastAPI (Python)  
- AI: Google ADK + Gemini-capable LLM (or equivalent)  
- Deploy: Docker → Cloud Run  
- Optional: Firestore for history

---

## Quick start (local)
```bash
git clone https://github.com/juliagarwal/healthsense-agent
cd healthsense-agent

python3 -m venv venv
source venv/bin/activate   # Windows: venv\\Scripts\\activate
pip install -r requirements.txt

export GOOGLE_APPLICATION_CREDENTIALS="/path/to/service-account.json"
export OPENAI_API_KEY="sk-..."   # or your Gemini/Vertex credentials

uvicorn app.main:app --reload --host 0.0.0.0 --port 8080
```

---

## Project layout
```
app/
  agent.py        # ADK agent + model config
  main.py         # FastAPI routes
  tools.py        # parsing utilities
  models/
    risk.py       # risk scoring logic
  utils/
    parser.py     # helpers (text/pdf)
Dockerfile
requirements.txt
README.md
```

---

## Deploy (Cloud Run)
```bash
gcloud builds submit --tag gcr.io/YOUR_PROJECT_ID/healthsense
gcloud run deploy healthsense \
  --image gcr.io/YOUR_PROJECT_ID/healthsense \
  --platform managed --region YOUR_REGION --allow-unauthenticated
```

Set your runtime environment variables (service account key, model/API keys) via Secret Manager or Cloud Run settings — do not commit secrets to the repo.

---

## Notes
- Outputs are informational only — not medical advice.  
- Use responsibly and do not run scans or data processing against systems you do not own.  

---

## Contact
Built by Juli Agrawal — https://github.com/juliagarwal/healthsense-agent
