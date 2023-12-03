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
      for i, match in enumerate(re.finditer(r'\*', self.engine.schematic.diagram), start=1):
        gear = Gear(
          id = i,
          line = self.engine.schematic.diagram.count('\n', 0, match.start()) + 1,
          start_column = match.start() - self.engine.schematic.diagram.rfind('\n', 0, match.start()),
          end_column = match.end() - self.engine.schematic.diagram.rfind('\n', 0, match.end()),
        )
        self.engine.gears.append(gear)
      return self.engine.gears
    except Exception as e:
      self.logger.log.exception(e)

  def get_parts(self) -> list[Part]:
    try:
      for match in re.finditer(r'\d+', self.engine.schematic.diagram):
        part = Part(
          number = match.group(),
          line = self.engine.schematic.diagram.count('\n', 0, match.start()) + 1,
          start_column = match.start() - self.engine.schematic.diagram.rfind('\n', 0, match.start()),
          end_column = match.end() - self.engine.schematic.diagram.rfind('\n', 0, match.end()),
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