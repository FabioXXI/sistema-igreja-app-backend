from sqlalchemy import Column, String, Integer, ForeignKey
from database.db import Base

class Login(Base):
    __tablename__ = 'logins'

    cpf = Column(String, ForeignKey('users.cpf'), primary_key=True)
    password = Column(String)
    perfil = Column(Integer)