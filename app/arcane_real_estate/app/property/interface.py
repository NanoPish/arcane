from datetime import datetime
from mypy_extensions import TypedDict


class PropertyInterface(TypedDict, total=False):
    property_id: int
    name: str
    description: str
    city: str
    type_id: int
