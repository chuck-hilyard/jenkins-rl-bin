
from app.spring_reader import SpringReader
import pytest

def test_spring_reader_instantiation():
    '''make sure the spring_reader instantiatiates successfully'''
    reader = SpringReader()
    assert isinstance(reader, SpringReader)


def test