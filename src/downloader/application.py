from PySide6.QtWidgets import QApplication

from . import views


class Application(QApplication):
    def __init__(self, args):
        super().__init__(args)
        self._main_window = views.MainWindow()

    @property
    def main_window(self):
        return self._main_window
