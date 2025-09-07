import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QLabel, QPushButton
from PySide6.QtCore import QSize, Qt

from layout_colorwidget import Color


class RightMenu(QWidget):
    def __init__(self):
        super().__init__()

        self.vlayout = QVBoxLayout(self)
        self.vlayout.setContentsMargins(0, 0, 0, 0)

        self.label = QLabel("CÓDIGOS QR PARA EXPO", alignment=Qt.AlignmentFlag.AlignCenter)
        self.vlayout.addWidget(self.label)

        self.vlayout.addWidget(Color("blue"))

        self.button = QPushButton("Generar")
        self.vlayout.addWidget(self.button)

        self.vlayout.addWidget(Color("blue"))



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        self.resize(QSize(800, 600))

        layout1 = QHBoxLayout()
        layout1.addWidget(Color("red"))
        layout1.addWidget(RightMenu())

        dummy_widget = QWidget()
        dummy_widget.setLayout(layout1)
        self.setCentralWidget(dummy_widget)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
