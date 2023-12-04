import models
import modules
from rich import print

class Day4:
  def __init__(self) -> None:
    self.config = models.Config()
    self.logger = modules.Logger()
    self.process_input()

  def process_input(self) -> None:
    try:
      print(self.config)
    except Exception as e:
      self.logger.log.exception(e)

if __name__ == "__main__":
    Day4()