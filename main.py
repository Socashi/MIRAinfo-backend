from fastapi import FastAPI
from pydantic import BaseModel
import databases

# Verbindung zur Datenbank
DATABASE_URL = "sqlite:///./database.db"
database = databases.Database(DATABASE_URL)

app = FastAPI()

# Datenbankverbindung herstellen und trennen
@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

# Standardroute
@app.get("/")
def read_root():
    return {"message": "Willkommen bei MIRAinfo-Backend!"}

# Erweiterte Suche mit Filter, einschließlich Tags
@app.get("/search")
async def search(query: str, category: str = None, language: str = "DE"):
    query_text = """
    SELECT * FROM information 
    WHERE (title LIKE :query OR content LIKE :query OR tags LIKE :query)
    AND (category = :category OR :category IS NULL)
    AND language = :language
    ORDER BY relevance DESC, date DESC
    """
    values = {"query": f"%{query}%", "category": category, "language": language}
    results = await database.fetch_all(query=query_text, values=values)
    return {"query": query, "results": results}