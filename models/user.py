from sqlalchemy import Column, String, Date, LargeBinary, ForeignKey
from sqlalchemy.orm import relationship
from database.db import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(String, primary_key=True)
    name = Column(String)
    cpf = Column(String, unique=True)
    birthday = Column(Date)
    email = Column(String, unique=True)
    profile_image = Column(LargeBinary)
    community_id = Column(String, ForeignKey('communities.id'))