from datetime import datetime
from mypy_extensions import TypedDict


class UserInterface(TypedDict, total=False):
    user_id: str
    first_name: str
    last_name: str
    birth_date: datetime
    mail: str
    password: str
