from humps import camel
from pydantic import BaseModel


def to_camel(string: str) -> str:
    """
    Func to create an alias from snake case variables
    """
    return str(camel.case(string))


class BaseServiceModel(BaseModel):
    """
    Base model to auto create a camelCase alias.
    Also allows population of Pydantic model via alias
    """

    class Config:
        """Config"""

        orm_mode = True
        alias_generator = to_camel
        allow_population_by_field_name = True
