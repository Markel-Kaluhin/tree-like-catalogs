from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.pool import AsyncAdaptedQueuePool, QueuePool

from settings.base import build_sqlalchemy_database_uri, settings

async_engine = create_async_engine(
    url=build_sqlalchemy_database_uri(),
    future=True,
    echo=False,
    echo_pool=False,
    pool_recycle=300,
    pool_pre_ping=True,
    poolclass=AsyncAdaptedQueuePool,
    connect_args={"server_settings": {"application_name": settings.application_name}},
)

async_session = sessionmaker(
    bind=async_engine,
    autocommit=False,
    autoflush=False,
    expire_on_commit=False,
    class_=AsyncSession,
)

sync_engine = create_engine(
    url=build_sqlalchemy_database_uri(),
    echo=False,
    echo_pool=False,
    pool_recycle=300,
    pool_pre_ping=True,
    poolclass=QueuePool,
    connect_args={"application_name": settings.application_name},
)

sync_session = sessionmaker(
    bind=sync_engine,
    autocommit=False,
    autoflush=False,
    expire_on_commit=False,
    class_=Session,
)
