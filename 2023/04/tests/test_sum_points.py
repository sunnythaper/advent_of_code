import os
import pytest
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import Day4 as main

def test_sum_points_default() -> None:
  app = main()
  scratchcards = app.get_scratchcards()
  assert app.sum_points(scratchcards) == 26443

def test_sum_points_test_1() -> None:
  app = main('data/input_test_1.txt')
  scratchcards = app.get_scratchcards()
  assert app.sum_points(scratchcards) == 13