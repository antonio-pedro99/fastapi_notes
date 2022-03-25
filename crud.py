from typing import List
from fastapi import APIRouter
import database as db
from models import Note, NoteIn, NoteUp

router = APIRouter()

@router.get("/notes/", response_model = List[Note], tags=["Notes"])
async def read_notes():
    return db.engine.execute(db.notes.select()).fetchall()

@router.get("/notes/{note_id}",tags=["Notes"] )
async def get_note_by_id(note_id:int):
    return db.engine.execute(db.notes.select().where(db.notes.c.id == note_id)).first()


@router.post("/notes/", response_model = Note, tags=["Notes"])
async def create_note(note: NoteIn):
    query = db.engine.execute(db.notes.insert().values(text = note.text, completed = note.completed))
    return db.engine.execute(db.notes.select().where(db.notes.c.id == query.lastrowid)).first()


@router.put("/notes/{note_id}", response_model=Note,  tags=["Notes"])
async def update_note(note:NoteUp, note_id:int):
    db.engine.execute(db.notes.update().where(db.notes.c.id == note_id).values(completed= note.completed))
    return  db.engine.execute(db.notes.select().where(db.notes.c.id == note_id)).first()


@router.delete("/notes/{note_id}", response_model = List[Note], tags=["Notes"])
async def delete_note(note_id: int):
    db.engine.execute(db.notes.delete().where(db.notes.c.id == note_id))
    return db.engine.execute(db.notes.select()).fetchall()