import math
import models
import modules
from rich import print

class Day4:
  def __init__(self, file: str = None) -> None:
    self.config = models.Config()
    self.logger = modules.Logger()
    if file:
      self.config.input.file = file

  def get_scratchcards(self) -> models.Scratchcards:
    try:
      with open(self.config.input.file, "r") as file:
        scratchcards = models.Scratchcards()
        for line in file:
          card = line.replace('Card', '').strip().split(":")
          number = card[0]
          sets = card[1].strip().split("|")
          winning_numbers = [int(num) for num in sets[0].strip().split(" ") if num.strip()]
          played_numbers = [int(num) for num in sets[1].strip().split(" ") if num.strip()]
          matched_numbers = len(set(winning_numbers).intersection(played_numbers))
          points = math.pow(2, matched_numbers - 1) if matched_numbers > 0 else 0
          scratchcards.cards.append(models.Card(
            number = number,
            winning_numbers = winning_numbers,
            played_numbers = played_numbers,
            matched_numbers = matched_numbers,
            points = points
          ))
      return scratchcards
    except Exception as e:
      self.logger.log.exception(e)

  def sum_points(self, scratchcards: models.Scratchcards) -> int:
    sum = 0
    for card in scratchcards.cards:
      sum += card.points
    return sum

if __name__ == "__main__":
    app = Day4()
    scratchcards = app.get_scratchcards()
    print(app.sum_points(scratchcards))