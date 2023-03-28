import pytest

import main

@pytest.fixture
def get_arguments():
    return {"keyword": "test"}


def test_get_keyword(get_arguments):
    assert main.get_keyword(arguments=get_arguments) == "test"

def test_get_keyword_no_arguments():
    assert main.get_keyword() == None

def get_keyword(arguments={}):
    assert main.get_keyword(arguments=arguments) == "test"

