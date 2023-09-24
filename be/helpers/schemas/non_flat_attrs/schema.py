from datetime import datetime
from decimal import Decimal
from typing import List, Optional

from pydantic import Field

from helpers.schemas.base import BaseServiceModel


class NonFlatAttrsPropertyCreateSchema(BaseServiceModel):
    id: Optional[int]
    name: str
    value: Decimal


class NonFlatAttrsPropertySchema(NonFlatAttrsPropertyCreateSchema):
    created_at: datetime


class NonFlatAttrsNodeSchema(BaseServiceModel):
    id: int
    parent_id: Optional[int]
    name: str
    children: Optional[List["NonFlatAttrsNodeSchema"]] = Field(default_factory=list)
    properties: Optional[List[NonFlatAttrsPropertySchema]] = Field(default_factory=list)
    created_at: datetime
