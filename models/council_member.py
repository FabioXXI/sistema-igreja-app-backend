from sqlalchemy import Column, String, ForeignKey
from database.db import Base

class CouncilMember(Base):
    __tablename__ = 'council_members'

    id = Column(String, primary_key=True)
    office = Column(String)
    cpf = Column(String, ForeignKey('users.cpf'))