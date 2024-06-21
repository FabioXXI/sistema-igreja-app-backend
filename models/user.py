from sqlalchemy import Column, String, Date, LargeBinary, ForeignKey
from sqlalchemy.orm import relationship
from database.db import Base

class User(Base):
    __tablename__ = 'users'

    name = Column(String)
    cpf = Column(String, primary_key=True)
    birthday = Column(Date)
    email = Column(String)
    profile_image = Column(LargeBinary)
    community_id = Column(String, ForeignKey('communities.id'))