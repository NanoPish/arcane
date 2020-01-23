from datetime import datetime
from mypy_extensions import TypedDict


class RoomInterface(TypedDict, total=False):
    name: str
    description: str
    property_id: int
