from pydantic import BaseModel, FilePath

class Logging(BaseModel):
    level: str = 'INFO'
    format: str = '%(message)s'
    date_format: str = '%b %dth, %Y %I:%M:%S %p'
    handler: str = 'rich'
    rich_tracebacks: bool = True
    show_locals: bool = True

class Schematic(BaseModel):
    # file: FilePath = 'data/test_list.txt'
    file: FilePath = 'data/list.txt'

class Filter(BaseModel):
    part: str = r'\d+'
    gear: str = r'\*'
    symbol: str = r'[^.\d]'

class Config(BaseModel):
    filter: Filter = Filter()
    logging: Logging = Logging()
    schematic: Schematic = Schematic()
