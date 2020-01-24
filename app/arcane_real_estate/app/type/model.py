from sqlalchemy import Integer, Column, String
from .. import db  # noqa
from .interface import TypeInterface


class Type(db.Model):
    """A Arcanific Type"""

    __tablename__ = "type"
    type_id = Column(Integer(), primary_key=True)
    name = Column(String(255), nullable=False)
    description = Column(String(255), nullable=False)

    def update(self, changes):
        for key, val in changes.items():
            if key not in ["type_id"]:
                setattr(self, key, val)
        return
