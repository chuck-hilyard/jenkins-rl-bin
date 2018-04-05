
import pytest
import sys
from spring_config_parser import main

@pytest.fixture()
def instantiate_main():
  main2 = main.Main()
  return main2

@pytest.fixture()
def instantiate_main_with_bad_arg(ARGV='-x'):
  main2 = main.Main()
  sys.argv[1] = ARGV
  main2.validate_args()


def test_pass_no_cli_args(instantiate_main):
  '''ensure we get a help message when no args are passed'''
  assert instantiate_main

def test_pass_bad_cli_args(instantiate_main_with_bad_arg):
  '''pass a bad arg get the default help message'''
  with pytest.raises(SystemExit) as e:
    instantiate_main_with_bad_arg()
    assert e.type == SystemExit
    assert e.value == 2

def test_validate_arg_syntax():
  '''ensure the args passed are syntactically correct'''
  sys.argv = ['project', 'environment', 'platform']
  main2 = main.Main()


