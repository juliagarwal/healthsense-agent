import os
from pathlib import Path

from dotenv import load_dotenv
from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
import google.auth

from app.tools import TOOLS

# --- FIX 1: Configure your API Key ---
# The ADK will likely need your Google API key. The best practice is
# to set it as an environment variable.
# Make sure to run `export GOOGLE_API_KEY='YOUR_API_KEY'` in your terminal
# before running the script.
# This line configures the underlying generative AI library.
genai.configure(api_key=os.environ["GEMINI_API_KEY"])


# --- FIX 2: Correct Model Name ---
# The model name "gemini-2.5-flash" is incorrect. 
# The correct name for the Gemini Flash model is "gemini-1.5-flash".
gemini_model = GeminiModel(
    # Use the correct model name from the Gemini family
    model="gemini-1.5-flash", 
    temperature=0.2,
)

health_agent = Agent(
    name="healthsense_agent",
    model=gemini_model,
    description="AI-powered health assistant for prescription and general guidance.",
    instruction="""
You are HealthSense, a helpful and responsible health assistant.
You:
1. Analyze prescriptions (text or image)
2. Extract medicine info using tools
3. Save results into Firestore
4. Give safe, friendly health advice
5. Never diagnose diseases

Follow a step-by-step approach.
""",
    tools=TOOLS
)

# Set as root agent
runtime = AgentRuntime(health_agent)
