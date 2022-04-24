"""Pytest: utils modules"""
from pathlib import Path

import pytest

from rainbowdrinkinggame.utils import create_markdown, export_markdown


def test_create_markdown_generel():
    input_dict = {
        'players': ['P1', 'P2', 'P3', 'P4', 'P5'],
        'sips': [1,2,3,4,5],
        'shots': [5,4,3,2,1]
        }
    output = create_markdown(input_dict)
    assert isinstance(output, str)

def test_create_markdown_less_players():
    input_dict = {
        'players': ['P1', 'P2', 'P3', 'P4'],
        'sips': [1,2,3,4,5],
        'shots': [5,4,3,2,1]
        }
    with pytest.raises(AssertionError) as excinfo:
        create_markdown(input_dict)
    assert "Player Count needs to be 5" in str(excinfo.value)

def test_create_markdown_less_sips():
    input_dict = {
        'players': ['P1', 'P2', 'P3', 'P4', 'P5'],
        'sips': [1,2,3,4],
        'shots': [5,4,3,2,1]
        }
    with pytest.raises(AssertionError) as excinfo:
        create_markdown(input_dict)
    assert "Sips count needs to be equal player count" in str(excinfo.value)

def test_create_markdown_less_shots():
    input_dict = {
        'players': ['P1', 'P2', 'P3', 'P4', 'P5'],
        'sips': [1,2,3,4,5],
        'shots': [5,4,3,2]
        }
    with pytest.raises(AssertionError) as excinfo:
        create_markdown(input_dict)
    assert "Shots count needs to be equal player count" in str(excinfo.value)

def test_export_markdown_generel(fs):
    input_str = """
# Header1

- item1
- item2

test text
    """
    directory = Path('/test/test.html')
    fs.create_file(directory)
    assert directory.exists()
    with open(directory, 'r', encoding="utf8") as file:
        assert len(file.readlines()) == 0
    export_markdown(input_str, directory)
    with open(directory, 'r', encoding="utf8") as file:
        assert len(file.readlines()) > 0
        