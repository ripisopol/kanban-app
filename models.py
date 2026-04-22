from sqlalchemy import Column, Integer, String
from database import Base

class Card(Base):
    __tablename__ = "cards"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, default="")
    column = Column(String, default="todo")