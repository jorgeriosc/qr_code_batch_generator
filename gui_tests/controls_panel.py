from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QCheckBox, QPushButton

from file_selector import FileSelector
from color_widget import ColorWidget


class ControlsPanel(QWidget):
    def __init__(self):
        super().__init__()

        self.vlayout = QVBoxLayout()
        self.vlayout.setContentsMargins(0, 0, 0, 0)

        self.label1 = QLabel("CÓDIGOS QR PARA EXPO", alignment=Qt.AlignmentFlag.AlignCenter)
        self.vlayout.addWidget(self.label1)

        self.vlayout.addWidget(ColorWidget("blue"))

        self.file_selector = FileSelector()
        self.vlayout.addWidget(self.file_selector)

        self.checkbox = QCheckBox("Colocar código QR")
        self.vlayout.addWidget(self.checkbox)

        self.vlayout.addWidget(ColorWidget("blue"))

        self.generate_button = QPushButton("Siguiente ->")
        self.vlayout.addWidget(self.generate_button)

        self.setLayout(self.vlayout)
