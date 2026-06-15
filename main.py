from fastapi import FastAPI, Request
import os
from dotenv import load_dotenv
import requests

load_dotenv()

app = FastAPI()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_API_URL = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}"

@app.get("/")
def read_root():
    return {"status": "Real Estate Assistant bot is alive"}

@app.get("/check-keys")
def check_keys():
    return {
        "anthropic_key_loaded": bool(os.getenv("ANTHROPIC_API_KEY")),
        "telegram_token_loaded": bool(os.getenv("TELEGRAM_BOT_TOKEN"))
    }
@app.post("/webhook")
async def telegram_webhook(request: Request):
    data = await request.json()
    
    chat_id = data["message"]["chat"]["id"]
    text = data["message"].get("text", "")
    
    # For now, just echo back what we received
    reply = f"You said: {text}"
    
    requests.post(f"{TELEGRAM_API_URL}/sendMessage", json={
        "chat_id": chat_id,
        "text": reply
    })
    
    return {"ok": True}