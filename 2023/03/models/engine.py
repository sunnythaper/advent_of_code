from pydantic import BaseModel

class Gear(BaseModel):
    id: int
    line: int
    start_column: int
    end_column: int
    ratio: int = 0

class Part(BaseModel):
    number: int
    line: int
    start_column: int
    end_column: int
    gear_ids: list[int] = []

class Schematic(BaseModel):
    diagram: str

class Sum(BaseModel):
    parts: int = 0
    gears: int = 0

class Engine(BaseModel):
    schematic: Schematic
    gears: list[Gear] = []
    parts: list[Part] = []
    sum: Sum = Sum()