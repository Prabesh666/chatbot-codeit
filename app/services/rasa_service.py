# Logic for interacting with Rasa
import aiohttp

RASA_URL = "http://localhost:5005/webhooks/rest/webhook"

async def get_rasa_response(message: str):
    async with aiohttp.ClientSession() as session:
        async with session.post(RASA_URL, json={"sender": "user", "message": message}) as resp:
            data = await resp.json()
            # Rasa response is a list of messages
            return " ".join([item.get("text", "") for item in data])
