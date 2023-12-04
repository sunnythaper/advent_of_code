from pydantic import BaseModel, FilePath

class Logging(BaseModel):
    level: str = 'INFO'
    format: str = '%(message)s'
    date_format: str = '%b %dth, %Y %I:%M:%S %p'
    handler: str = 'rich'
    rich_tracebacks: bool = True
    show_locals: bool = True

class Input(BaseModel):
    file: FilePath = 'data/input.txt'

class Config(BaseModel):
    logging: Logging = Logging()
    input: Input = Input()