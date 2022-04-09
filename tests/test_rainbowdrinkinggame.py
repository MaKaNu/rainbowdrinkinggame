"""Test module for rainbowdrinkinggame."""

from rainbowdrinkinggame import __author__, __email__, __version__


def test_project_info():
    """Test __author__ value."""
    assert __author__ == "Matti Kaupenjohann"
    assert __email__ == "matti.kaupenjohann@fh-dortmund.de"
    assert __version__ == "0.0.0"
