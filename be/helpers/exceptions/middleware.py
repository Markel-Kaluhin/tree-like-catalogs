import json

from starlette.requests import Request
from starlette.responses import JSONResponse

from helpers.exceptions.base import BaseServiceException
from helpers.schemas.common.notification import (
    Notification,
    NotificationPayload,
    NotificationType,
)


async def general_exception_handler(_: Request, exc: Exception) -> JSONResponse:
    status_code = 500
    content = json.loads(
        Notification(
            type=NotificationType.error,
            payload=NotificationPayload(
                status=0, code=status_code, message=str(exc), title="Server Error"
            ),
        ).json()
    )
    return JSONResponse(content=content, status_code=status_code)


async def base_exception_handler(_: Request, exc: BaseServiceException) -> JSONResponse:
    content = json.loads(
        Notification(
            type=NotificationType.error,
            payload=NotificationPayload(
                code=exc.status_code,
                message=exc.detail,
                title=exc.title,
                url=exc.url,
                status=exc.status,
            ),
        ).json()
    )

    return JSONResponse(content=content, status_code=exc.status_code)
