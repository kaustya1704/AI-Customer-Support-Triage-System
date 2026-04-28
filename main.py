from fastapi import FastAPI
from pydantic import BaseModel
import requests

app = FastAPI()

OPENROUTER_API_KEY = "YOUR_API_KEY"

class EmailInput(BaseModel):
    message: str

@app.post("/analyze")
def analyze_email(data: EmailInput):

    prompt = f"""
You are an AI customer support assistant.

Analyze this email and return STRICT JSON:

- intent: refund / exchange / complaint / inquiry / escalate
- urgency: low / medium / high
- sentiment: positive / neutral / negative
- confidence: 0 to 1
- uncertainty: true/false
- reply_en: natural English reply
- reply_ar: natural Arabic reply

If unclear → uncertainty = true

Email:
{data.message}
"""

    response = requests.post(
        url="https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {OPENROUTER_API_KEY}"
        },
        json={
            "model": "meta-llama/llama-3.3-70b-instruct:free",
            "messages": [{"role": "user", "content": prompt}]
        }
    )

    return response.json()