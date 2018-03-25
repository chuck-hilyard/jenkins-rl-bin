
import pytest
from spring_config_parser import main

@pytest.fixture()
  def instantiate_main():
    main2 = main.Main()

def test_instantiate_main(instantiate_main):
  '''returns an instance of Main'''
  main2 = main.Main()

def test_cli_args():
  '''ensures we're getting the right args'''
  assert main2.validate_args('arg1', 'arg2', 'arg3') == True

def test_cli_no_args():
  '''ensures that if no args are passed that we give a help message and exit'''
  pass