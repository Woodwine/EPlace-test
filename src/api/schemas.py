from typing import Optional, List

from pydantic import BaseModel
from bson import ObjectId

from src.core.schemas import Key, Notification


class BaseRequest(BaseModel):
    user_id: ObjectId


class ListRequest(BaseRequest):
    skip: int = 0
    limit: int = 0


class CreateRequest(BaseRequest):
    target_id: Optional[ObjectId]
    key: Key
    data: Optional[dict]


class ReadRequest(BaseRequest):
    notification_id: ObjectId


class ResponseData(BaseModel):
    elements: int
    new: int
    request: ListRequest
    list: List[Notification | None]


class Response(BaseModel):
    success: bool = True


class ListResponse(Response):
    data: ResponseData

