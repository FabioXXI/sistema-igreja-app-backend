from sqlalchemy import Column, String, ForeignKey, Date
from database.db import Base

class Session(Base):
    __tablename__ = 'sessions'

    user_id = Column(String, ForeignKey('users.id'), primary_key=True)
    session_token = Column(String)
    last_activity = Column(Date)