import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import Day4 as main

def test_process_input() -> None:
  assert main().process_input() == 'Day 4'

def test_process_input_alt() -> None:
  assert main('data/test_input.txt').process_input() == 'Test Input'
