from sqlalchemy import DECIMAL, Column, ForeignKey, Integer, String, func

from helpers.entity.sql_entity import TZDateTime
from helpers.models import Base


class Node(Base):
    __tablename__ = "node"

    id = Column(Integer, primary_key=True)
    parent_id = Column(Integer, ForeignKey("node.id"), index=True)
    name = Column(String(256), nullable=False, index=True)
    created_at = Column(TZDateTime, nullable=False, server_default=func.now())
    updated_at = Column(TZDateTime, nullable=False, server_default=func.now())


class Property(Base):
    __tablename__ = "property"

    id = Column(Integer, primary_key=True)
    node_id = Column(Integer, ForeignKey("node.id"), index=True)
    name = Column(String(256), nullable=False, index=True)
    value = Column(DECIMAL, nullable=False)
    created_at = Column(TZDateTime, nullable=False, server_default=func.now())
    updated_at = Column(TZDateTime, nullable=False, server_default=func.now())
