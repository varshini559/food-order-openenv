from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/")
def home():
    return {"message": "ByteBites API running"}

@app.post("/reset")
async def reset(request: Request):
    data = await request.json()
    return {
        "status": "success",
        "message": "Environment reset successful"
    }
