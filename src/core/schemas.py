from enum import Enum
from typing import Optional
from uuid import UUID, uuid4
from datetime import datetime
from bson import ObjectId

from pydantic import BaseModel, Field


class Key(str, Enum):
    registration = "registration"
    new_message = "new_message"
    new_post = "new_post"
    new_login = "new_login"


class Notification(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    timestamp: datetime = datetime.now()
    is_new: bool = False
    user_id: ObjectId
    key: Key
    target_id: Optional[ObjectId]
    data: Optional[dict]
