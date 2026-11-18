from fastapi import FastAPI
from dotenv import load_dotenv

load_dotenv()

from router.chatbot import chat_router

app = FastAPI()

app.include_router(chat_router)