# rainbowdrinkinggame package

## Submodules

## rainbowdrinkinggame.rainbowdrinkinggame module

Rainbow Drinking Game Main Module

This module creates a pyside6 Window Application for the
“Rainbow Drinking Game”. It helps to document the player activitate
for the game and exports the statistics at the end of the game as html file.

Example:

    To run the Application just go into the root directory and call:

    > $ python rainbowdrinkinggame/rainbowdrinkinggame.py

Todo:

    
    * add style_rc


### _class_ rainbowdrinkinggame.rainbowdrinkinggame.Bridge()
Bases: `PySide6.QtCore.QObject`


#### create_result(players, sips, shots)
the create_result method uses the given data to export the html statistics.
This Method self accepts more than 5 Players but will fail in the lower called
util functions.

Args:

    players (List(str)): A List with 5 Player names
    sips (List(str)): A List with 5 sip statistics
    shots (List(str)): A List with 5 shot statistics


* **Return type**

    `None`



#### minus(value)
The minus method substracts 1 from the str input and returns the result as str.

Args:

    value (str): A numeric uint8 string value

Returns:

    str: The Substraction of value by 1, or “0” if value is already “0”.


* **Return type**

    `str`



#### plus(value)
The plus method adds 1 to the str input and returns the result as str.

Args:

    value (str): A numeric uint8 string value

Returns:

    str: The Sum of value and 1


* **Return type**

    `str`



#### staticMetaObject(_ = <PySide6.QtCore.QMetaObject object_ )
## rainbowdrinkinggame.utils module

Rainbow Drinking Game Util Functions

This Module includes function which will be utilized by the Bridge Slot Methods.
The functions are mainly used inside slots methods, but can also be used outside
the methods.

Todo:

    
    * All Fine for the moment.


### rainbowdrinkinggame.utils.create_markdown(player_values)
This Function creates a multiline string based on a dictinary

The dictionary has to follow some strict rules,
since the game “rainbowdrinkinggame allows only 5 Players.

Args:

    player_values (Dict[str, Union[List[str], List[int]]]): The dictinary which includes

        the player values:


            * PlayerNames


            * PlayerSips


            * PlayerShots

Returns:

    str: a multiline markdownstyle str


* **Return type**

    `str`



### rainbowdrinkinggame.utils.export_markdown(md_str, path)
Function to export a given markdown string to given path.

Args:

    md_str (str): A String in Markdown Format
    path (Path): Path variable for the html output


* **Return type**

    `None`


## Module contents

RainbowDrinkingGame namespace.
