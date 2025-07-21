# main.py

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow frontend to access backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can specify frontend URL here
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "MediResponder backend running!"}

@app.post("/process")
async def process_data(request: Request):
    data = await request.json()
    user_message = data.get("message", "")
    
    # You can add real AI logic here
    ai_response = f"🧠 AI suggests: For '{user_message}', please apply basic first-aid and remain calm."
    
    return {"reply": ai_response}
