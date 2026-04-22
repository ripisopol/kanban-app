from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
from database import  get_db
from models import Card

app = FastAPI()

@app.on_event("startup")
def startup():
    from database import Base, engine
    Base.metadata.create_all(bind=engine)

@app.get("/health")
def health():
    return {"status": "ok"}

class CardSchema(BaseModel):
    title: str
    description: Optional[str] = ""
    column: str = "todo"

@app.get("/cards")
def get_cards():
    db = get_db()
    return db.query(Card).all()

@app.post("/cards", status_code=201)
def create_card(card: CardSchema):
    db = get_db()
    new_card = Card(
        title=card.title,
        description=card.description,
        column=card.column
    )
    db.add(new_card)
    db.commit()
    db.refresh(new_card)
    return new_card

class CardUpdateSchema(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    column: Optional[str] = None

@app.patch("/cards/{card_id}")
def update_card(card_id: int, card: CardUpdateSchema):
    db = get_db()
    db_card = db.query(Card).filter(Card.id == card_id).first()
    if not db_card:
        raise HTTPException(status_code=404, detail="Card not found")
    if card.title is not None:
        db_card.title = card.title
    if card.description is not None:
        db_card.description = card.description
    if card.column is not None:
        db_card.column = card.column
    db.commit()
    db.refresh(db_card)
    return db_card

@app.delete("/cards/{card_id}", status_code=204)
def delete_card(card_id: int):
    db = get_db()
    db_card = db.query(Card).filter(Card.id == card_id).first()
    if not db_card:
        raise HTTPException(status_code=404, detail="Card not found")
    db.delete(db_card)
    db.commit()
    return None
