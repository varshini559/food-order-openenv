from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/")
def home():
    return {"message": "API running"}

@app.post("/reset")
async def reset(request: Request):
    data = await request.json()
    return {"status": "success"}
