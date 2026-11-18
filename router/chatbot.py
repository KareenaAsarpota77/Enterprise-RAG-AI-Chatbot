from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db

chat_router = APIRouter()


@chat_router.get("/test-db")
def test_db(db: Session = Depends(get_db)):

    try:
        db.execute("SELECT 1")
        return {"message": "Database connected successfully!"}

    except Exception as e:
        return {"error": str(e)}