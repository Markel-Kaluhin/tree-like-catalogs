import enum
from typing import Optional

from pydantic import Field

from helpers.schemas.base import BaseServiceModel


class NotificationType(enum.Enum):
    success = "success"
    info = "info"
    warning = "warning"
    error = "error"


class NotificationPayload(BaseServiceModel):
    status: int
    url: Optional[str] = Field(default=None)
    code: int
    message: str
    is_custom: bool = Field(default=False)
    title: Optional[str] = Field(default="")


class Notification(BaseServiceModel):
    type: NotificationType
    payload: NotificationPayload
