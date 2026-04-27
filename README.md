# AI Customer Support Triage System (EN + AR)

## Summary
This project builds an AI-powered system that classifies customer emails into intent, urgency, and sentiment, and generates suggested replies in English and Arabic.

---

## Setup (under 5 minutes)

1. Clone repo
2. Install dependencies:
   pip install -r requirements.txt

3. Add OpenRouter API key in main.py

4. Run:
   uvicorn main:app --reload

5. Open:
   http://127.0.0.1:8000/docs

---

## Features

- Intent classification (refund, exchange, complaint, etc.)
- Urgency detection
- Sentiment analysis
- Multilingual response (EN + AR)
- Uncertainty handling

---

## Evals

Test cases include:
- Normal refund request
- Angry complaint
- Arabic input
- Mixed language
- Garbage input
- Medical case → should escalate

Failures:
- Model sometimes overconfident
- Arabic quality depends on prompt tuning

---

## Tradeoffs

- Used free OpenRouter model instead of paid APIs
- No fine-tuning due to time constraint
- No UI, focused on backend correctness

---

## Tooling

- OpenRouter + Llama 3.3 70B
- FastAPI backend
- Prompt engineering

---

## Future Improvements

- Add RAG with FAQ database
- Add UI dashboard
- Improve eval scoring metrics