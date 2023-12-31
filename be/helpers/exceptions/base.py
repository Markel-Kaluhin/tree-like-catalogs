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
        custom_message: Optional[str] = "Base Exception",
    ) -> None:
        super().__init__(status_code=code, detail=custom_message)
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


class NonFlatAttrsException(BaseEntityException):
    def __init__(
        self,
        code: int = 404,
        url: Optional[str] = None,
        custom_message: Optional[str] = None,
    ) -> None:
        super().__init__(
            title="NonFlatAttrs Exception",
            code=code,
            url=url,
            status=ExceptionType.non_flat_attrs,
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
