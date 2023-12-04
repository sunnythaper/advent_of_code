import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import Day4 as main

def test_main() -> None:
  assert main().process_input() == 'Day 4'
