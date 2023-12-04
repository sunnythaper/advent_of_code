import models
import modules
from rich import print

class Day4:
  def __init__(self) -> None:
    self.config = models.Config()
    self.logger = modules.Logger()

  def process_input(self) -> str:
    try:
      print(self.config)
      return 'Day 4'
    except Exception as e:
      self.logger.log.exception(e)

if __name__ == "__main__":
    Day4().process_input()