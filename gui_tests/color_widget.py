from PySide6.QtGui import QColor, QPalette
from PySide6.QtWidgets import QWidget


class ColorWidget(QWidget):
    def __init__(self, color):
        super().__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)
