import os
import pytest
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import Day4 as main

def test_process_input_default() -> None:
  assert main().process_input() == 'Day 4'

def test_process_input_test_1() -> None:
  assert main('data/input_test_1.txt').process_input() == 'Test Input'

def test_process_input_empty() -> None:
  assert main('data/input_test_empty.txt').process_input() == ''

def test_process_input_invalid() -> None:
  with pytest.raises(FileNotFoundError, match='No such file or directory'):
    raise FileNotFoundError('No such file or directory')