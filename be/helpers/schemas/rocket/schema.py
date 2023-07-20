from datetime import datetime
from decimal import Decimal
from typing import List, Optional

from pydantic import Field

from helpers.schemas.base import BaseServiceModel


class RockerPropertyCreateSchema(BaseServiceModel):
    id: Optional[int]
    name: str
    value: Decimal


class RockerPropertySchema(RockerPropertyCreateSchema):
    created_at: datetime


class RocketNodeSchema(BaseServiceModel):
    id: int
    parent_id: Optional[int]
    name: str
    children: Optional[List['RocketNodeSchema']] = Field(default_factory=list)
    properties: Optional[List[RockerPropertySchema]] = Field(default_factory=list)
    created_at: datetime
