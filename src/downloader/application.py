from PySide6.QtWidgets import QApplication, QWidget


class Application(QApplication):
    def __init__(self, args):
        super().__init__(args)

    def get_main_window(self):
        w = QWidget()
        w.resize(800, 600)
        return w
