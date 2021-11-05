from fastapi import FastAPI, HTTPException
from schemas import MessageOut, MessageIn
import crud

app = FastAPI()


@app.get("/ping")
def pong():
    return {"message": "pong"}


@app.post("/messages", response_model=MessageOut)
def add_message(msg_in: MessageIn):
    return crud.add_message(msg_in)


@app.get("/messages/{id}", response_model=MessageOut)
def get_message(id: int):
    msg = crud.get_message(id)
    if msg:
        return msg
    raise HTTPException(404, f"Message with id={id} not found")


@app.get("/messages", response_model=list[MessageOut])
def get_messages():
    return crud.get_messages()


@app.put("/messages/{id}", response_model=MessageOut)
def update_message(id: int, msg_in: MessageIn):
    msg = crud.update_message(id, msg_in)
    if msg:
        return msg
    raise HTTPException(404, f"Message with id={id} not found")


@app.delete("/messages/{id}", response_model=MessageOut)
def delete_message(id: int):
    msg = crud.delete_message(id)
    if msg:
        return msg
    raise HTTPException(404, f"Message with id={id} not found")
