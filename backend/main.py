from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import traceback

from backend.models import ChatRequest, ChatResponse
from backend.database import load_csv_to_db
from backend.agent import get_agent

app = FastAPI(title="Foydalanuvchilar Chatbot API", version="1.0.0")

# Allow requests from the frontend (same server or localhost dev)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def startup_event():
    """Load CSV data into SQLite when the server starts."""
    print("🚀 Server starting — loading data into SQLite...")
    load_csv_to_db()
    # Warm up the agent (loads model)
    get_agent()
    print("✅ Agent ready!")


@app.get("/")
async def serve_frontend():
    """Serve the chat UI."""
    return FileResponse("frontend/index.html")


@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    """
    Main chat endpoint.
    Accepts a natural language question, runs it through the SQL Agent,
    returns a natural language answer.
    """
    if not request.message.strip():
        raise HTTPException(status_code=400, detail="Message cannot be empty")

    try:
        agent = get_agent()
        result = agent.invoke({"input": request.message})
        answer = result.get("output", "Javob topilmadi.")
        return ChatResponse(answer=answer)

    except Exception as e:
        traceback.print_exc()
        raise HTTPException(
            status_code=500,
            detail=f"Agent xatosi: {str(e)}"
        )


@app.get("/health")
async def health():
    return {"status": "ok"}