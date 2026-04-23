from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = "users"

    id            = Column(Integer, primary_key=True, index=True)
    username      = Column(String, unique=True, nullable=False, index=True)
    password_hash = Column(String, nullable=False)

    cards = relationship("Card", back_populates="user")

class Card(Base):
    __tablename__ = "cards"

    id          = Column(Integer, primary_key=True, index=True)
    title       = Column(String, nullable=False)
    description = Column(String, default="")
    column      = Column(String, default="todo")
    user_id     = Column(Integer, ForeignKey("users.id"), nullable=False)

    user = relationship("User", back_populates="cards")
