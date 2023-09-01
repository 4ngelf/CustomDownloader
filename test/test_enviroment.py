import pytest


@pytest.mark.parametrize("package", ["PySide6"])
def test_checkModules(package):
    __import__(package)
