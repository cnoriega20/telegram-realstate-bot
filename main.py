from fastapi import FastAPI
import os
from dotenv import load_dotenv
load_dotenv()

app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "Real Estate Assistant bot is alive"}

@app.get("/check-keys")
def check_keys():
    return {
        "anthropic_key_loaded": bool(os.getenv("ANTHROPIC_API_KEY")),
        "telegram_token_loaded": bool(os.getenv("TELEGRAM_BOT_TOKEN"))
    }