import re

from models.config import Config
from models.engine import Engine, Gear, Part, Schematic
from modules.log import Logger
from rich import print

class Day3:
  def __init__(self) -> None:
    self.config = Config()
    self.logger = Logger()
    self.process_engine_schematic()

  def process_engine_schematic(self) -> Engine:
    try:
      with open(self.config.schematic.file, "r") as schematic:
        self.engine = Engine(
          schematic = Schematic(
            diagram = schematic.read(),
          )
        )
      self.get_gears()
      self.get_parts()
      self.sum_parts()
      print(self.engine)
      return self.engine
    except Exception as e:
      self.logger.log.exception(e)

  def get_gears(self) -> list[Gear]:
    try:
      for i, gear in enumerate(re.finditer(r'\*', self.engine.schematic.diagram), start=1):
        gear = Gear(
          id = i,
          line = self.engine.schematic.diagram.count('\n', 0, gear.start()) + 1,
          start_column = gear.start() - self.engine.schematic.diagram.rfind('\n', 0, gear.start()),
          end_column = gear.end() - self.engine.schematic.diagram.rfind('\n', 0, gear.end()),
        )
        self.engine.gears.append(gear)
      return self.engine.gears
    except Exception as e:
      self.logger.log.exception(e)

  def get_parts(self) -> list[Part]:
    try:
      for part in re.finditer(r'\d+', self.engine.schematic.diagram):
        part = Part(
          number = part.group(),
          line = self.engine.schematic.diagram.count('\n', 0, part.start()) + 1,
          start_column = part.start() - self.engine.schematic.diagram.rfind('\n', 0, part.start()),
          end_column = part.end() - self.engine.schematic.diagram.rfind('\n', 0, part.end()),
        )
        if self.check_valid_part(part):
          self.engine.parts.append(part)
      return self.engine.parts
    except Exception as e:
      self.logger.log.exception(e)

  def check_valid_part(self, part: Part) -> bool:
    try:
      lines = self.engine.schematic.diagram.split('\n')
      start_line = max(0, part.line - 1)
      end_line = min(len(lines), part.line + 2)
      return any(self.check_for_symbols(part, lines[line_number - 1], line_number) for line_number in range(start_line, end_line))
    except Exception as e:
      self.logger.log.exception(e)

  def check_for_symbols(self, part: Part, line: str, line_number: int) -> bool:
    try:
      start_column = max(0, part.start_column - 2)
      symbols = bool(re.search(r'[^.\d]', line[start_column:part.end_column]))
      if symbols:
        self.check_for_gears(part, line, line_number)
      return symbols
    except Exception as e:
      self.logger.log.exception(e)

  def check_for_gears(self, part: Part, line: str, line_number: int) -> bool:
    try:
      start_column = max(0, part.start_column - 2)
      gears = re.finditer(r'[\*]', line[start_column:part.end_column])
      for gear in gears:
        part.gear_ids.append(self.get_gear_id(gear, line, line_number))
    except Exception as e:
      self.logger.log.exception(e)

  def get_gear_id(self, gear, line: str, line_number: int) -> int:
    try:
      for known_gear in self.engine.gears:
        if known_gear.line == line_number:
          return known_gear.id
    except Exception as e:
      self.logger.log.exception(e)

  def sum_parts(self) -> int:
    try:
      for part in self.engine.parts:
        self.engine.sum += int(part.number)
      return self.engine.sum
    except Exception as e:
      self.logger.log.exception(e)

if __name__ == "__main__":
  Day3()