from models.config import config
from modules.log import logger
from rich import print

class Day3:
  def __init__(self) -> None:
    self.config = config
    self.process_input()

  def process_input(self) -> None:
    try:
      print(self.config)
    except Exception as e:
      logger.exception(e)

if __name__ == "__main__":
  Day3()