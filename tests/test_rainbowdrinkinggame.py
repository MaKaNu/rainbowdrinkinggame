"""Test module for rainbowdrinkinggame."""
import pytest


from rainbowdrinkinggame import (
    __author__,
    __email__,
    __version__
)
from rainbowdrinkinggame.rainbowdrinkinggame import (
    QML_IMPORT_NAME,
    QML_IMPORT_MAJOR_VERSION,
    Bridge
)


def test_project_info():
    """Test __author__ value."""
    assert __author__ == "Matti Kaupenjohann"
    assert __email__ == "matti.kaupenjohann@fh-dortmund.de"
    assert __version__ == "0.0.0"
    
def test_qml_globals():
    """Test QML Specific Global Variables
    """
    assert QML_IMPORT_MAJOR_VERSION == 1
    assert QML_IMPORT_NAME == "io.qt.textproperties"

def test_bridge_plus():
    bridge = Bridge()
    output = bridge.plus(1)
    assert output == "2"
    assert isinstance(output, str)

def test_bridge_minus():
    bridge = Bridge()
    output = bridge.minus(2)
    output_zero = bridge.minus(0)
    assert output == "1"
    assert output_zero == "0"
    assert isinstance(output, str)
    
def test_bridge_create_result(mocker):
    mocker.patch(
        'rainbowdrinkinggame.utils.create_markdown',
        """# HEADER""")
    mocker.patch(
        'rainbowdrinkinggame.utils.export_markdown',
        None
    )
    bridge = Bridge()
    output = bridge.create_result(
        ('P1', 'P2', 'P3', 'P4', 'P5'),
        (1,1,1,1,1),
        (1,1,1,1,1)
    )
    assert output is None
