
from app.spring_reader import SpringReader
import pytest

def test_spring_reader_instantiation():
    '''make sure the spring_reader instantiatiates successfully'''
    reader = SpringReader()
    assert isinstance(reader, SpringReader)


def test_spring_reader_request(httpserver):
    httpserver.serve_content(open('cached-content.html').read())
    assert httpserver.code == 200