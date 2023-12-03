import re

from models.config import Config
from models.engine import Engine, Part
from modules.log import Logger
from rich import print
import re

class Day3:
  def __init__(self) -> None:
    self.config = Config()
    self.logger = Logger()
    self.process_engine_schematic()

  def process_engine_schematic(self) -> Engine:
    try:
      with open(self.config.schematic.file, "r") as schematic:
        self.schematic = schematic.read()
        parts = self.get_parts()
        self.engine = Engine(parts=parts)
        self.sum_parts()
        print(self.engine)
        return self.engine
    except Exception as e:
      self.logger.log.exception(e)

  def get_parts(self) -> list[Part]:
    try:
      parts = []
      for match in re.finditer(r'\d+', self.schematic):
        part_number = match.group()
        line_number = self.schematic.count('\n', 0, match.start()) + 1
        column_number = match.start() - self.schematic.rfind('\n', 0, match.start())
        part = Part(number=part_number, line=line_number, column=column_number)
        if self.check_valid_part(part):
          parts.append(part)
      return parts
    except Exception as e:
      self.logger.log.exception(e)

  def check_valid_part(self, part: Part) -> bool:
    try:
      lines = self.schematic.split('\n')
      current_line = lines[part.line - 1]

      if part.column == 1 and re.search(r'[^.\d]', current_line[part.column - 1:part.column + len(str(part.number))]):
        return True

      if part.column > 1 and re.search(r'[^.\d]', current_line[part.column - 2:part.column + len(str(part.number))]):
        return True

      if part.line > 1:
        above_line = lines[part.line - 2]

        if part.column == 1 and re.search(r'[^.\d]', above_line[part.column - 1:part.column + len(str(part.number))]):
          return True

        if part.column > 1 and re.search(r'[^.\d]', above_line[part.column - 2:part.column + len(str(part.number))]):
          return True

      if part.line < len(lines):
        below_line = lines[part.line]

        if part.column == 1 and re.search(r'[^.\d]', below_line[part.column - 1:part.column + len(str(part.number))]):
          return True

        if part.column > 1 and re.search(r'[^.\d]', below_line[part.column - 2:part.column + len(str(part.number))]):
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