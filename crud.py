from typing import List, Optional

from fastapi import FastAPI, APIRouter
import database as db
from models import Note, NoteIn

router = APIRouter()

@router.get("/notes/", response_model = List[Note])
async def read_notes():
    query = db.notes.select()
    return await db.database.fetch_all(query)

@router.post("/notes/", response_model = Note)
async def create_note(note: NoteIn):
    query = db.notes.insert().values(text = note.text, completed = note.completed)
    last_id = await db.database.execute(query)
    return {**note.dict(), "id": last_id}


# @router.delete("/notes/{note_id}", response_model = List[Note])
# async def delete_note(note_id: int):
    