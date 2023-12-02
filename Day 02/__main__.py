import re

from pydantic import BaseModel
from rich import print

class Round(BaseModel):
    red_cubes: int | None = None
    green_cubes: int | None = None
    blue_cubes: int | None = None

class Game(BaseModel):
    id: int
    possible: bool | None = None
    rounds: list[Round] | None = None

class Day2:
    def __init__(self) -> None:
      self.total_red_cubes = 12
      self.total_green_cubes = 13
      self.total_blue_cubes = 14
      self.file = "list.txt"
      self.games = []
      self.sum = 0
      self.process_games()
      self.sum_possible()
      print(self.games)
      print(self.sum)

    def process_games(self) -> None:
      with open(self.file, "r") as file:
        for line in file:
          id = re.match(r"Game (\d+):", line).group(1)
          rounds = self.process_rounds(line)
          self.games.append(Game(id=id, rounds=rounds))
      self.check_possible()

    def process_rounds(self, line: str) -> list[Round]:
      rounds = []
      for round in re.finditer(r"((?:(?:\d+) (?:red|green|blue)(?:, )?)+)", line):
        cube_matches = re.findall(r"(\d+) (red|green|blue)", round.group(1))
        red_cubes = 0
        green_cubes = 0
        blue_cubes = 0
        for cubes, color in cube_matches:
          if color == "red":
            red_cubes += int(cubes)
          elif color == "green":
            green_cubes += int(cubes)
          elif color == "blue":
            blue_cubes += int(cubes)
        rounds.append(Round(
          red_cubes=red_cubes,
          green_cubes=green_cubes,
          blue_cubes=blue_cubes,
        ))
      return rounds

    def check_possible(self) -> None:
      for game in self.games:
        for round in game.rounds:
          if round.red_cubes > self.total_red_cubes or round.green_cubes > self.total_green_cubes or round.blue_cubes > self.total_blue_cubes:
            game.possible = False
          else:
            if game.possible is None:
              game.possible = True

    def sum_possible(self) -> None:
      for game in self.games:
        if game.possible:
          self.sum += game.id

if __name__ == "__main__":
    Day2()