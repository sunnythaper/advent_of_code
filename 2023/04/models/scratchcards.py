from pydantic import BaseModel

class Card(BaseModel):
    number: int
    winning_numbers: list[int]
    played_numbers: list[int]
    matched_numbers: int
    points: int

class Scratchcards(BaseModel):
    cards: list[Card] = []