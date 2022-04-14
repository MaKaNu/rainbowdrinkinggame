from rainbowdrinkinggame.utils import create_markdown, export_markdown

import pytest
from pathlib import Path
#import pyfakefs
import html5lib

def test_create_markdown_generel():
    input = {
        'players': ['P1', 'P2', 'P3', 'P4', 'P5'],
        'sips': [1,2,3,4,5],
        'shots': [5,4,3,2,1]
        }
    output = create_markdown(input)
    assert isinstance(output, str)

def test_create_markdown_less_players():
    input = {
        'players': ['P1', 'P2', 'P3', 'P4'],
        'sips': [1,2,3,4,5],
        'shots': [5,4,3,2,1]
        }
    with pytest.raises(AssertionError) as excinfo:
        create_markdown(input)
    assert "Player Count needs to be 5" in str(excinfo.value)

def test_create_markdown_less_sips():
    input = {
        'players': ['P1', 'P2', 'P3', 'P4', 'P5'],
        'sips': [1,2,3,4],
        'shots': [5,4,3,2,1]
        }
    with pytest.raises(AssertionError) as excinfo:
        create_markdown(input)
    assert "Sips count needs to be equal player count" in str(excinfo.value)

def test_create_markdown_less_shots():
    input = {
        'players': ['P1', 'P2', 'P3', 'P4', 'P5'],
        'sips': [1,2,3,4,5],
        'shots': [5,4,3,2]
        }
    with pytest.raises(AssertionError) as excinfo:
        create_markdown(input)
    assert "Shots count needs to be equal player count" in str(excinfo.value)

def test_export_markdown_generel(fs):
    input = """
# Header1

- item1
- item2

test text
    """
    dir = Path('/test/test.html')
    fs.create_file(dir)
    output = export_markdown(input, dir)
    assert dir.exists()
    html5parser = html5lib.HTMLParser()
    html5parser.parse(output)