from fastapi import FastAPI

app = FastAPI()

@app.post("/analyze")
def analyze(data: dict):
    text = data["text"]
    words = text.split()

    return {
        "word_count": len(words),
"keywords": words
    }
