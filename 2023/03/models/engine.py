from pydantic import BaseModel

class Part(BaseModel):
    number: int
    line: int
    column: int

class Engine(BaseModel):
    parts: list[Part] | None = None
    sum: int = 0