from pydantic import BaseModel

class NoteIn(BaseModel):
    text: str
    completed: bool


class NoteUp(BaseModel):
    completed: bool
    
class Note(BaseModel):
    id: int
    text: str
    completed: bool

    class Config:
        orm_mode = True