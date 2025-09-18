from fastapi import APIRouter, HTTPException
from app.models.message import Message
from app.services.rasa_service import get_rasa_response

router = APIRouter()

@router.post("/message")
async def send_message(msg: Message):
    """
    Send user message to Rasa chatbot and get response.
    """
    try:
        response = await get_rasa_response(msg.text)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
