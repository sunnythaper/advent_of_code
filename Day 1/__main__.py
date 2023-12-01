import re

class Day01:
  def __init__(self) -> None:
    self.sum = 0
    self.list = []
    with open("list.txt", "r") as file:
        for line in file:
            self.list.append(line.strip())
    self.process_list()

  def process_list(self) -> list:
    self.strip_alpha_characters()
    self.strip_middle_digits()
    self.repeat_single_digits()
    self.sum_list()
    print(self.sum)

  def strip_alpha_characters(self) -> list:
    list = []
    for line in self.list:
        line = re.sub("[a-zA-Z]", "", line)
        list.append(line)
    self.list = list

  def strip_middle_digits(self) -> list:
    list = []
    for line in self.list:
        line = re.sub(r"^(\d).*?(\d)$", r"\1\2", line)
        list.append(line)
    self.list = list

  def repeat_single_digits(self) -> list:
    list = []
    for line in self.list:
        line = re.sub(r"^(\d)$", r"\1\1", line)
        list.append(line)
    self.list = list

  def sum_list(self) -> int:
    for line in self.list:
        self.sum += int(line)

if __name__ == "__main__":
    Day01()
