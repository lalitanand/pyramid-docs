import bcrypt
from sqlalchemy import (
    Column,
    Integer,
    Text,
)

from .meta import Base


class User(Base):
    """ The SQLAlchemy declarative model class for a User object. """
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False, unique=True)
    role = Column(Text, nullable=False)

    password_hash = Column(Text)

    def set_password(self, pw, pre_hashed=False):
        if pre_hashed:
            pwhash = pw
        else:
            pwhash = bcrypt.hashpw(pw, bcrypt.gensalt())
        self.password_hash = pwhash

    def check_password(self, pw):
        return bcrypt.hashpw(pw, self.password_hash) == self.password_hash
