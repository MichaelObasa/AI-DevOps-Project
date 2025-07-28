from fastapi import FastAPI, Request
from pydantic import BaseModel
import datetime
import hashlib
import os

app = FastAPI()

class PromptInput(BaseModel):
    prompt: str

@app.post("/prompt")
async def get_response(input: PromptInput):
    prompt = input.prompt
    version_id = hashlib.sha256(prompt.encode()).hexdigest()[:8]
    timestamp = datetime.datetime.now().isoformat()

    # Fake response
    response = f"Mock GPT response to: {prompt}"
    tokens_used = len(prompt.split()) + len(response.split())

    # Save prompt version
    with open(f"prompts/{version_id}.txt", "w") as f:
        f.write(prompt)

    # Log token usage
    with open("logs/token_usage.csv", "a") as log:
        log.write(f"{timestamp},{version_id},{tokens_used},{prompt[:30]}...\n")

    return {
        "version_id": version_id,
        "response": response,
        "tokens_used": tokens_used
    }
