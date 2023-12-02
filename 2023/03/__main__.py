from models.config import Config
from modules.log import Logger
from rich import print

class Day3:
  def __init__(self) -> None:
    try:
      self.config = Config()
      self.logger = Logger()
      self.process_input()
    except Exception as e:
      self.logger.log.exception(e)

  def process_input(self) -> None:
    try:
      print(self.config)
    except Exception as e:
      self.logger.log.exception(e)

if __name__ == "__main__":
  Day3()