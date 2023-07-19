from typing import Optional

from starlette.exceptions import HTTPException

from helpers.schemas.common.enums import ExceptionType


class BaseServiceException(HTTPException):
    def __init__(
        self,
        title: str,
        code: int,
        status: int,
        url: Optional[str] = None,
        custom_message: Optional[str] = None,
    ) -> None:
        super().__init__(status_code=code, detail="Base Exception")
        self.title = title
        self.url = url
        self.status = status


class BaseEntityException(BaseServiceException):
    def __init__(
        self,
        title: str,
        code: int,
        status: int,
        url: Optional[str] = None,
        custom_message: Optional[str] = None,
    ) -> None:
        super().__init__(
            title=title,
            code=code,
            url=url,
            status=status,
            custom_message=custom_message,
        )


class RocketException(BaseEntityException):
    def __init__(
        self,
        code: int = 404,
        url: Optional[str] = None,
        custom_message: Optional[str] = None,
    ) -> None:
        super().__init__(
            title="Rocker Exception",
            code=code,
            url=url,
            status=ExceptionType.rocket,
            custom_message=custom_message,
        )


class RepositoryException(BaseServiceException):
    def __init__(
        self,
        code: int = 404,
        url: Optional[str] = None,
        custom_message: Optional[str] = None,
    ) -> None:
        super().__init__(
            title="Repository Exception",
            code=code,
            url=url,
            status=ExceptionType.repository,
            custom_message=custom_message,
        )
