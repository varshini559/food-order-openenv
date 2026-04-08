from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "ByteBites API Running"}

@app.post("/reset")
def reset():
    return {"status": "reset successful"}
