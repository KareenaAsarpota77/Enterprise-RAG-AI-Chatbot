
from database import engine, Base
from models import Document, DocumentChunk, ChatHistory

try:

    Base.metadata.create_all(bind=engine)

    print("Database connected successfully!")
    print("Tables created successfully!")

except Exception as e:

    print("Error:", e)
