from typing import List

from beanie import Document
from pydantic import EmailStr

from src.core.schemas import Notification


class User(Document):
    email: EmailStr
    notifications: List[Notification | None]

    class Collection:
        name = "users"
