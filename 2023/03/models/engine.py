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

class Engine(BaseModel):
    gears: list[Gear] = []
    parts: list[Part] = []
    schematic: Schematic
    sum: int = 0