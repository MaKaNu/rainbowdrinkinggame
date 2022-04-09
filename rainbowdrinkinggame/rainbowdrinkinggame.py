import sys
from pathlib import Path

from PySide6.QtCore import QObject, Slot
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine, QmlElement
from PySide6.QtQuickControls2 import QQuickStyle

from utils import create_markdown, export_markdown
# import style_rc

# To be used on the @QmlElement decorator
# (QML_IMPORT_MINOR_VERSION is optional)
QML_IMPORT_NAME = "io.qt.textproperties"
QML_IMPORT_MAJOR_VERSION = 1


@QmlElement
class Bridge(QObject):
    @Slot(str, result=str)
    def plus(self, value):
        return str(int(value) + 1)

    @Slot(str, result=str)
    def minus(self, value):
        if int(value) == 0:
            return str(0)
        return str(int(value) - 1)

    @Slot(list, list, list)
    def create_result(self, players, sips, shots):
        if len(players) != len(sips) != len(shots):
            assert "Error in view.qml!"
        player_values = {"players": players, "sips": sips, "shots": shots}
        markdown_str = create_markdown(player_values)
        html_path = Path(__file__).parent.parent / "output.html"
        export_markdown(markdown_str, html_path)


if __name__ == "__main__":
    app = QGuiApplication(sys.argv)
    QQuickStyle.setStyle("Material")
    engine = QQmlApplicationEngine()

    # Get the path of the current directory, and then add the name
    # of the QML file, to load it.
    qml_file = Path(__file__).parent / "view.qml"
    engine.load(qml_file)

    if not engine.rootObjects():
        sys.exit(-1)

    sys.exit(app.exec())
