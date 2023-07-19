from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, func

from helpers.entity.sql_entity import TZDateTime
from helpers.models import Base


class RocketNode(Base):
    __tablename__ = "rocket_node"

    id = Column(Integer, primary_key=True)
    parent_id = Column(Integer, ForeignKey("rocket_node.id"), index=True)
    name = Column(String(256), nullable=False)
    created_at = Column(TZDateTime, nullable=False, server_default=func.now())
    updated_at = Column(TZDateTime, nullable=False, server_default=func.now())


class RocketProperty(Base):
    __tablename__ = "rocket_property"

    id = Column(Integer, primary_key=True)
    rocket_node_id = Column(Integer, ForeignKey("rocket_node.id"), index=True)
    name = Column(String(256), nullable=False)
    value = Column(DECIMAL, nullable=False)
    created_at = Column(TZDateTime, nullable=False, server_default=func.now())
    updated_at = Column(TZDateTime, nullable=False, server_default=func.now())
