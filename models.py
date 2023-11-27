from sqlalchemy import Column, Integer, String
from database import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(20), unique=True)
    password = Column(String(20))

    def __init__(self, username=None, password=None):
        self.username = username
        self.password = password

    def __repr__(self):
        return "<User(id=%d, username='%s', password='%s')>" % (self.id, self.username, self.password)

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'password': self.password
        }
