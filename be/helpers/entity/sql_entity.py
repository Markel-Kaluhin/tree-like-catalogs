import datetime

from sqlalchemy import Column, DateTime, Integer, TypeDecorator, func
from sqlalchemy.orm import DeclarativeMeta, registry

mapper_registry = registry()


class Base(metaclass=DeclarativeMeta):
    __abstract__ = True

    registry = mapper_registry
    metadata = mapper_registry.metadata
    timezone = True


class TZDateTime(TypeDecorator):
    impl = DateTime
    cache_ok = True

    def process_bind_param(self, value, dialect):
        if value is not None:
            if not value.tzinfo:
                raise TypeError("tzinfo is required")
            value = value.astimezone(datetime.timezone.utc).replace(tzinfo=None)
        return value

    def process_result_value(self, value, dialect):
        if value is not None:
            value = value.replace(tzinfo=datetime.timezone.utc)
        return value


class SqlEntity(Base):
    __abstract__ = True

    id = Column(Integer, primary_key=True)
    created_date = Column(TZDateTime, nullable=False, server_default=func.now())
    modified_date = Column(
        TZDateTime,
        nullable=False,
        server_default=func.now(),
        onupdate=func.current_timestamp(),
    )

    def __str__(self) -> str:
        return str(self.id)

    def __repr__(self) -> str:
        return str(self.__dict__)
