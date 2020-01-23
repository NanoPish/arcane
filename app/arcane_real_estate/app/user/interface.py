from datetime import datetime
from mypy_extensions import TypedDict


class UserInterface(TypedDict, total=False):
    name: str
    description: str
