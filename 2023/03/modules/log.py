import logging

from models.config import Config
from rich.logging import RichHandler

class Logger:
  def __init__(self) -> None:
    self.config = Config()
    self.log = self.setup_logging()

  def setup_logging(self) -> None:
    logging.basicConfig(
      level=self.config.logging.level,
      format=self.config.logging.format,
      datefmt=self.config.logging.date_format,
      handlers=[
        RichHandler(
          rich_tracebacks=self.config.logging.rich_tracebacks,
          tracebacks_show_locals=self.config.logging.show_locals,
        )
      ],
    )
    return logging.getLogger("rich")