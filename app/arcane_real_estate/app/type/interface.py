from datetime import datetime
from mypy_extensions import TypedDict


class TypeInterface(TypedDict, total=False):
    name: str
    description: str
