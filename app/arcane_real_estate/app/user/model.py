from sqlalchemy import Integer, Column, String, Date
from sqlalchemy.orm import relationship
from app import db  # noqa
from passlib.hash import pbkdf2_sha256


class User(db.Model):
    """A Arcanific User"""

    __tablename__ = "user"
    user_id = Column(Integer(), primary_key=True)
    first_name = Column(String(255), nullable=False)
    last_name = Column(String(255), nullable=False)
    birth_date = Column(Date, nullable=False)
    mail = db.Column(db.String(64), index=True, nullable=False, unique=True)
    password_hash = db.Column(db.String(128), nullable=False)

    properties = relationship("Property", back_populates="user")

    def update(self, changes):
        for key, val in changes.items():
            setattr(self, key, val)
        return

    def hash_password(self, password) -> None:
        self.password_hash = pbkdf2_sha256.hash(password)

    def verify_password(self, password) -> bool:
        return pbkdf2_sha256.verify(password, self.password_hash)
