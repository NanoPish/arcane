from sqlalchemy import Integer, Column, String, ForeignKey
from sqlalchemy.orm import relationship
from app import db  # noqa
from .interface import PropertyInterface


class Property(db.Model):
    """A Arcanific Property"""

    __tablename__ = "property"
    property_id = Column(Integer(), primary_key=True)
    name = Column(String(255), nullable=False)
    description = Column(String(255), nullable=False)
    city = Column(String(255), nullable=False)
    type_id = Column(Integer, ForeignKey('type.type_id'), nullable=False)
    user_id = Column(Integer, ForeignKey('user.user_id'))

    rooms = relationship("Room")
    type = relationship("Type")
    user = relationship("User", back_populates="properties")

    def update(self, changes):
        for key, val in changes.items():
            setattr(self, key, val)
        return