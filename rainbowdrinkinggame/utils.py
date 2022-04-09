"""Util methods"""
from markdown import markdown

def create_markdown(player_values):
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
    
def export_markdown(md_str, path):
    html = markdown(md_str)
    with open(path, 'w') as f:
        f.write(html)
