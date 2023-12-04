import models
import modules
from rich import print

class Day4:
  def __init__(self, file: str = None) -> None:
    self.config = models.Config()
    self.logger = modules.Logger()
    if file:
      self.config.input.file = file

  def process_input(self) -> str:
    try:
      with open(self.config.input.file, "r") as file:
        self.input = file.read()
      print(self.config)
      print(self.input)
      return self.input
    except Exception as e:
      self.logger.log.exception(e)

if __name__ == "__main__":
    Day4().process_input()