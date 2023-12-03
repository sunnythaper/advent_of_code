from pydantic import BaseModel

class Part(BaseModel):
    number: int
    line: int
    start_column: int
    end_column: int

class Gear(BaseModel):
    id: int
    line: int
    column: int
    ratio: int = 0

class Engine(BaseModel):
    gears: list[Gear]
    parts: list[Part]
    sum: int = 0