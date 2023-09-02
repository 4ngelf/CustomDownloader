import sys

from .application import Application

__version__ = "0.1.0"


def startapp():
    app = Application(sys.argv)
    app.main_window.show()
    sys.exit(app.exec())
