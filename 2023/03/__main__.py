import re

from models.config import Config
from models.engine import Engine, Gear, Part
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
        self.schematic = schematic.read()
      self.engine = Engine(
        gears = self.get_gears(),
        parts = self.get_parts(),
      )
      self.sum_parts()
      print(self.engine)
      return self.engine
    except Exception as e:
      self.logger.log.exception(e)

  def get_gears(self) -> list[Gear]:
    try:
      gears = []
      for i, match in enumerate(re.finditer(r'\*', self.schematic), start=1):
        gear = Gear(
          id = i,
          line = self.schematic.count('\n', 0, match.start()) + 1,
          column = match.start() - self.schematic.rfind('\n', 0, match.start()),
        )
        gears.append(gear)
      return gears
    except Exception as e:
      self.logger.log.exception(e)

  def get_parts(self) -> list[Part]:
    try:
      parts = []
      for match in re.finditer(r'\d+', self.schematic):
        part = Part(
          number = match.group(),
          line = self.schematic.count('\n', 0, match.start()) + 1,
          start_column = match.start() - self.schematic.rfind('\n', 0, match.start()),
          end_column = match.end() - self.schematic.rfind('\n', 0, match.end()),
        )
        if self.check_valid_part(part):
          parts.append(part)
      return parts
    except Exception as e:
      self.logger.log.exception(e)

  def check_valid_part(self, part: Part) -> bool:
    try:
      lines = self.schematic.split('\n')
      start_line = max(0, part.line - 1)
      end_line = min(len(lines), part.line + 2)
      return any(self.check_for_symbol(part, lines[line_number - 1]) for line_number in range(start_line, end_line))
    except Exception as e:
      self.logger.log.exception(e)

  def check_for_symbol(self, part: Part, line: str) -> bool:
    try:
      pattern = r'[^.\d]'

      if part.start_column == 1 and re.search(pattern, line[part.start_column - 1:part.end_column]):
        return True

      if part.start_column > 1 and re.search(pattern, line[part.start_column - 2:part.end_column]):
        return True

      return False
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