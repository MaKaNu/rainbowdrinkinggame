# -*- coding: utf-8 -*-
"""Rainbow Drinking Game Util Functions

This Module includes function which will be utilized by the Bridge Slot Methods.
The functions are mainly used inside slots methods, but can also be used outside
the methods.

Todo:
    * All Fine for the moment.

.. _Google Python Style Guide:
   http://google.github.io/styleguide/pyguide.html
"""
from pathlib import Path
from typing import Dict, Union, List

from markdown import markdown


def create_markdown(player_values:Dict[str, Union[List[str], List[int]]]) -> str:
    """This Function creates a multiline string based on a dictinary

    The dictionary has to follow some strict rules,
    since the game "rainbowdrinkinggame allows only 5 Players.

    Args:
        player_values (Dict[str, Union[List[str], List[int]]]): The dictinary which includes
            the player values:
                - PlayerNames
                - PlayerSips
                - PlayerShots

    Returns:
        str: a multiline markdownstyle str
    """
    assert len(player_values['players']) == 5, "Player Count needs to be 5"
    assert len(player_values['players']) == len(player_values['sips']), \
        "Sips count needs to be equal player count"
    assert len(player_values['players']) == len(player_values['shots']), \
        "Shots count needs to be equal player count"
    sips = player_values['sips']
    shots = player_values['shots']
    sips_sorted = sorted(sips, reverse=True)
    shots_sorted = sorted(shots, reverse=True)
    sip_sorted_idx = sorted(range(len(sips)), key=lambda k: sips[k], reverse=True)
    shot_sorted_idx = sorted(range(len(shots)), key=lambda k: shots[k], reverse=True)

    return f'''
# Ergebnis des Rainbow Drinking Tuniers

## Teilnehmer
* {player_values['players'][0]}
* {player_values['players'][1]}
* {player_values['players'][2]}
* {player_values['players'][3]}
* {player_values['players'][4]}

## Die meisten Schlücke
* {player_values['players'][sip_sorted_idx[0]]}: {sips_sorted[0]}
* {player_values['players'][sip_sorted_idx[1]]}: {sips_sorted[1]}
* {player_values['players'][sip_sorted_idx[2]]}: {sips_sorted[2]}
* {player_values['players'][sip_sorted_idx[3]]}: {sips_sorted[3]}
* {player_values['players'][sip_sorted_idx[4]]}: {sips_sorted[4]}

## Die meisten Shots
* {player_values['players'][shot_sorted_idx[0]]}: {shots_sorted[0]}
* {player_values['players'][shot_sorted_idx[1]]}: {shots_sorted[1]}
* {player_values['players'][shot_sorted_idx[2]]}: {shots_sorted[2]}
* {player_values['players'][shot_sorted_idx[3]]}: {shots_sorted[3]}
* {player_values['players'][shot_sorted_idx[4]]}: {shots_sorted[4]}
    '''

def export_markdown(md_str:str, path:Path)->None:
    """Function to export a given markdown string to given path.

    Args:
        md_str (str): A String in Markdown Format
        path (Path): Path variable for the html output
    """
    html = markdown(md_str)
    with open(path, 'w', encoding="utf8") as output_file:
        output_file.write(html)
