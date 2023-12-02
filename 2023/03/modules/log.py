import logging

from models.config import config
from rich.logging import RichHandler

logging.basicConfig(
    level=config.logging.level,
    format=config.logging.format,
    datefmt=config.logging.date_format,
    handlers=[
        RichHandler(
            rich_tracebacks=config.logging.rich_tracebacks,
            tracebacks_show_locals=config.logging.show_locals,
        )
    ],
)

logger = logging.getLogger("rich")
