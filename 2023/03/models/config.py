from pydantic import BaseModel

class Logging(BaseModel):
    level: str = 'INFO'
    format: str = '%(message)s'
    date_format: str = '%b %dth, %Y %I:%M:%S %p'
    rich_tracebacks: bool = True
    show_locals: bool = True

class Config(BaseModel):
    logging: Logging = Logging()

config = Config()
