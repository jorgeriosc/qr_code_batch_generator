from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel


class TemplateViewer(QWidget):
    def __init__(self):
        super().__init__()

        self.vlayout = QVBoxLayout()
        self.vlayout.setContentsMargins(0, 0, 0, 0)

        self.image_label = QLabel()
        self.vlayout.addWidget(self.image_label)

        self.setLayout(self.vlayout)

    def display_template(self, file_path):
        pixmap = QPixmap(file_path)
        scaled = pixmap.scaled(
            self.image_label.size(),
            aspectMode=Qt.KeepAspectRatio,
            mode=Qt.SmoothTransformation
        )

        self.image_label.setPixmap(scaled)
