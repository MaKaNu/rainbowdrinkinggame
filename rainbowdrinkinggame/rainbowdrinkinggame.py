# -*- coding: utf-8 -*-
""" Rainbow Drinking Game Main Module

This module creates a pyside6 Window Application for the
"Rainbow Drinking Game". It helps to document the player activitate
for the game and exports the statistics at the end of the game as html file.

Example:
    To run the Application just go into the root directory and call:

        $ python rainbowdrinkinggame/rainbowdrinkinggame.py

Todo:
    * add style_rc

.. _Google Python Style Guide:
   http://google.github.io/styleguide/pyguide.html
"""

import sys
from pathlib import Path
import logging
from typing import List

from PySide6.QtCore import QObject, Slot
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine, QmlElement
from PySide6.QtQuickControls2 import QQuickStyle

from rainbowdrinkinggame.utils import create_markdown, export_markdown

# import style_rc

# To be used on the @QmlElement decorator
# (QML_IMPORT_MINOR_VERSION is optional)
QML_IMPORT_NAME = "io.qt.textproperties"
QML_IMPORT_MAJOR_VERSION = 1


@QmlElement
class Bridge(QObject):
    """Pyside6 Bridge Object for Signals/Slots in the QML"""

    # TODO result=str causes mypy issues
    @Slot(str, result=str)  # type: ignore
    def plus(self, value: str) -> str:
        """The plus method adds 1 to the str input and returns the result as str.

        Args:
            value (str): A numeric uint8 string value

        Returns:
            str: The Sum of value and 1
        """
        logging.debug("%s: slot method 'plus': value=%s", self.__str__, value)
        return str(int(value) + 1)

    # TODO result=str causes mypy issues
    @Slot(str, result=str)  # type: ignore
    def minus(self, value: str) -> str:
        """The minus method substracts 1 from the str input and returns the result as str.

        Args:
            value (str): A numeric uint8 string value

        Returns:
            str: The Substraction of value by 1, or "0" if value is already "0".
        """
        logging.debug("%s: slot method 'minus': value=%s", self.__str__, value)
        if int(value) == 0:
            return str(0)
        return str(int(value) - 1)

    @Slot(list, list, list)
    def create_result(self, players: List[str], sips: List[str], shots: List[str]) -> None:
        """the create_result method uses the given data to export the html statistics.
        This Method self accepts more than 5 Players but will fail in the lower called
        util functions.

        Args:
            players (List(str)): A List with 5 Player names
            sips (List(str)): A List with 5 sip statistics
            shots (List(str)): A List with 5 shot statistics
        """
        logging.debug(
            "%s: slot method 'minus': players=%s, sips=%s, shots=%s",
            self.__str__,
            players,
            sips,
            shots,
        )
        player_values = {"players": players, "sips": sips, "shots": shots}
        markdown_str = create_markdown(player_values)
        html_path = Path(__file__).parent.parent / "output.html"
        export_markdown(markdown_str, html_path)


if __name__ == "__main__":
    app = QGuiApplication(sys.argv)  # pragma: no cover
    QQuickStyle.setStyle("Material")  # pragma: no cover
    engine = QQmlApplicationEngine()  # pragma: no cover

    # Get the path of the current directory, and then add the name
    # of the QML file, to load it.
    qml_file = Path(__file__).parent / "view.qml"  # pragma: no cover
    engine.load(qml_file)  # pragma: no cover

    if not engine.rootObjects():  # pragma: no cover
        sys.exit(-1)  # pragma: no cover

    sys.exit(app.exec())  # pragma: no cover
