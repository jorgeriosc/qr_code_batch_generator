import sys

from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QLabel, QPushButton, QCheckBox

from layout_colorwidget import Color
from file_selector import FileSelector

class RightMenu(QWidget):
    def __init__(self):
        super().__init__()

        self.vlayout = QVBoxLayout()
        self.vlayout.setContentsMargins(0, 0, 0, 0)

        self.label1 = QLabel("CÓDIGOS QR PARA EXPO", alignment=Qt.AlignmentFlag.AlignCenter)
        self.vlayout.addWidget(self.label1)

        self.vlayout.addWidget(Color("blue"))

        self.file_selector = FileSelector()
        self.vlayout.addWidget(self.file_selector)

        self.checkbox = QCheckBox("Colocar código QR")
        self.vlayout.addWidget(self.checkbox)

        self.vlayout.addWidget(Color("blue"))

        self.generate_button = QPushButton("Siguiente ->")
        self.vlayout.addWidget(self.generate_button)

        self.setLayout(self.vlayout)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QR Expo")
        # self.resize(QSize(800, 600))

        self.hlayout = QHBoxLayout()

        self.image_label = QLabel()
        self.hlayout.addWidget(self.image_label)
        
        self.right_menu = RightMenu()
        self.right_menu.file_selector.file_selected.connect(self.display_template)
        self.hlayout.addWidget(self.right_menu)

        dummy_widget = QWidget()
        dummy_widget.setLayout(self.hlayout)
        self.setCentralWidget(dummy_widget)

    def display_template(self, file_path):
        pixmap = QPixmap(file_path)
        scaled = pixmap.scaled(
            self.image_label.size(),
            aspectMode=Qt.KeepAspectRatio,
            mode=Qt.SmoothTransformation
        )
        self.image_label.setPixmap(scaled)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
