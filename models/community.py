from sqlalchemy import Column, String, LargeBinary
from sqlalchemy.orm import relationship
from database.db import Base

class Community(Base):
    __tablename__ = 'communities'

    id = Column(String, primary_key=True)
    localization = Column(String)
    email = Column(String, unique=True)
    community_image = Column(LargeBinary)
    patron = Column(String)

    warnings = relationship('Warning', backref='warnings', cascade="all, delete-orphan")