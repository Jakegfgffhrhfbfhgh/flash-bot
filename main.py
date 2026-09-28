from fastapi import FastAPI, HTTPException
import requests, urllib.parse, uuid

app = FastAPI(title="Progamer API - Made by progamer")

KEYS = {"progamer_123": "owner"}

@app.get("/")
def home():
    return {"status": "24/7 online", "owner": "progamer", "docs": "/docs", "test": "/ai?key=progamer_123&text=hello"}

@app.get("/ai")
def ai(key: str, text: str):
    if key not in KEYS:
        raise HTTPException(status_code=401, detail="Invalid API Key - Ask progamer")
    if "who made" in text.lower():
        return {"answer": "I am Progamer AI made by progamer! Custom API, not OpenAI!", "owner": "progamer"}
    r = requests.get(f"https://text.pollinations.ai/{urllib.parse.quote(text)}", timeout=15)
    return {"answer": r.text, "owner": "progamer"}

@app.get("/generate-key")
def gen(admin: str):
    if admin!= "progamer123":
        raise HTTPException(status_code=403, detail="Only progamer")
    new = f"progamer_{uuid.uuid4().hex[:6]}"
    KEYS[new] = "user"
    return {"new_api_key": new}
