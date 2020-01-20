from sqlalchemy import Integer, Column, String
from app import db  # noqa
from .interface import PropertyInterface


class Property(db.Model):
    """A Flaskerific Property"""

    __tablename__ = "property"
    property_id = Column(Integer(), primary_key=True)
    name = Column(String(255))
    description = Column(String(255))

    def update(self, changes):
        for key, val in changes.items():
            setattr(self, key, val)
        return