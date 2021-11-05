from pydantic import BaseModel, Field
from datetime import datetime


class MessageIn(BaseModel):
    text: str


class Message(MessageIn):
    id: int
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = None

    def update(self, msg_in: MessageIn):
        self.text = msg_in.text
        self.updated_at = datetime.now()


class MessageOut(Message):
    pass
