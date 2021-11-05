from schemas import Message, MessageIn
from itertools import count
from typing import Optional

MESSAGES: dict[int, Message] = {}
INT_SEQUENCE = count(1)


def add_message(msg_in: MessageIn) -> Message:
    msg = Message(id=next(INT_SEQUENCE), **msg_in.dict())
    MESSAGES[msg.id] = msg
    return msg


def get_message(id: int) -> Optional[Message]:
    return MESSAGES.get(id)


def get_messages() -> list[Message]:
    return list(MESSAGES.values())


def update_message(id: int, msg_in: MessageIn) -> Optional[Message]:
    msg = get_message(id)
    if msg:
        msg.update(msg_in)
        return msg


def delete_message(id: int) -> Optional[Message]:
    return MESSAGES.pop(id, None)
