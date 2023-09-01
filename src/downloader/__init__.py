import sys

from .application import Application


def startapp():
    app = Application(sys.argv)
    app.main_window.show()
    sys.exit(app.exec())
