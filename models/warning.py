from sqlalchemy import Column, String, Text, ForeignKey, Integer
from database.db import Base

class Warning(Base):
    __tablename__ = 'warnings'

    id = Column(String, primary_key=True)
    title = Column(String)
    description = Column(Text)
    community_id = Column(String, ForeignKey('communities.id'))
    coverage = Column(Integer)