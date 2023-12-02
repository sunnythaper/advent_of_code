import re

from pydantic import BaseModel
from rich import print

class Round(BaseModel):
    red_cubes: int | None = None
    green_cubes: int | None = None
    blue_cubes: int | None = None

class Game(BaseModel):
    id: int
    power: int | None = None
    possible: bool | None = None
    min_red_cubes: int | None = None
    min_green_cubes: int | None = None
    min_blue_cubes: int | None = None
    rounds: list[Round] | None = None

class Day2:
    def __init__(self) -> None:
      self.total_red_cubes = 12
      self.total_green_cubes = 13
      self.total_blue_cubes = 14
      self.file = "list.txt"
      self.games = []
      self.sum = 0
      self.power = 0
      self.process_games()
      print(self.games)
      print(self.sum)
      print(self.power)

    def process_games(self) -> None:
      with open(self.file, "r") as file:
        for line in file:
          id = re.match(r"Game (\d+):", line).group(1)
          rounds = self.process_rounds(line)
          self.games.append(Game(id=id, rounds=rounds))
      self.check_possible()
      self.sum_possible()
      self.minimum_needed_cubes()
      self.set_power()
      self.sum_power()

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

    def minimum_needed_cubes(self) -> None:
      for game in self.games:
        max_red_cubes = 0
        max_green_cubes = 0
        max_blue_cubes = 0
        for round in game.rounds:
          if round.red_cubes > max_red_cubes:
            max_red_cubes = round.red_cubes
          if round.green_cubes > max_green_cubes:
            max_green_cubes = round.green_cubes
          if round.blue_cubes > max_blue_cubes:
            max_blue_cubes = round.blue_cubes
        game.min_red_cubes = max_red_cubes
        game.min_green_cubes = max_green_cubes
        game.min_blue_cubes = max_blue_cubes

    def set_power(self) -> None:
      for game in self.games:
        game.power = game.min_red_cubes * game.min_green_cubes * game.min_blue_cubes

    def sum_power(self) -> None:
      for game in self.games:
        self.power += game.power

if __name__ == "__main__":
    Day2()