from PySide6.QtWidgets import QApplication, QMainWindow

from .visual.editor import VisualEditor


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('PyStudio')
        self.setCentralWidget(VisualEditor())


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    win = MainWindow()
    win.resize(960, 540)
    win.show()

    sys.exit(app.exec())
