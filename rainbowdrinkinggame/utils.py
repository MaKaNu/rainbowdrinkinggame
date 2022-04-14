"""Util methods"""
from pathlib import Path
from typing import Dict, Union, List

from markdown import markdown


def create_markdown(player_values:Dict[str, Union[List[str], List[int]]]):
    assert len(player_values['players']) == 5, "Player Count needs to be 5"
    assert len(player_values['players']) == len(player_values['sips']), f"Sips count needs to be equal player count"
    assert len(player_values['players']) == len(player_values['shots']), f"Shots count needs to be equal player count"
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
    
def export_markdown(md_str:str, path:Path):
    html = markdown(md_str)
    with open(path, 'w') as f:
        f.write(html)
