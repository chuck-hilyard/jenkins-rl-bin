
import pytest
from spring_config_parser import main

@pytest.fixture()
def instantiate_main():
  main2 = main.Main()
  return main2

def test_pass_no_args(instantiate_main):
  '''ensure we get a help message when the no args are passed'''
  with pytest.raises(SystemExit) as e:
    instantiate_main.validate_args()
  assert e.type == SystemExit
  assert e.value.code == 2


def test_pass_bad_args(instantiate_main):
  '''ensure we get an error when passing bad arguments'''
  with pytest.raises(SystemExist) as e:
    instantiate_main.validate_args()
