from typing import List
from fastapi import FastAPI

from model.notein import NoteIn
from model.note import Note
from config.db import database, notes


app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.get("/notes/", response_model=List[Note])
async def read_notes():
    query = notes.select()
    return await database.fetch_all(query)


@app.post("/notes/", response_model=Note)
async def create_note(note: NoteIn):
    query = notes.insert().values(content=note.content, created=note.created)
    last_record_id = await database.execute(query)
    return {
        **note.dict(),
        "id": last_record_id
    }
