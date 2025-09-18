from fastapi import FastAPI
from app.routes import chatbot

app = FastAPI(title="Rasa Chatbot API")

# Include chatbot routes
app.include_router(chatbot.router, prefix="/chatbot", tags=["Chatbot"])
