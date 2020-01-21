from datetime import datetime
from mypy_extensions import TypedDict


class PropertyInterface(TypedDict, total=False):
    name: str
    description: str
    city: str
