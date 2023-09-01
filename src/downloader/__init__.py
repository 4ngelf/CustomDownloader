import sys

from .application import Application


def startapp():
    app = Application(sys.argv)
    main_window = app.get_main_window()
    main_window.show()
    sys.exit(app.exec())
