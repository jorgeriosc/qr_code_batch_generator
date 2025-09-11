from pathlib import Path
from PySide6.QtCore import Signal
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QLabel, QFileDialog


class FileSelector(QWidget):
    file_selected = Signal(str)

    def __init__(self):
        super().__init__()

        self.hlayout = QHBoxLayout()
        self.hlayout.setContentsMargins(0, 0, 0, 0)

        self.select_button = QPushButton("Seleccionar plantilla")
        self.select_button.clicked.connect(self.open_file_dialog)
        self.hlayout.addWidget(self.select_button)

        self.file_name_label = QLabel("Sin seleccionar")
        self.hlayout.addWidget(self.file_name_label)
        
        self.setLayout(self.hlayout)

    def open_file_dialog(self):
        file_path, _ = QFileDialog.getOpenFileName(
            parent=self,
            caption="Seleccionar plantilla",
            dir="..",
            filter="PNG (*.png)"
        )

        if file_path:
            file_name = Path(file_path).name
            self.file_name_label.setText(file_name)
            self.file_selected.emit(file_path)


if __name__ == "__main__":
    app = QApplication([])
    window = QMainWindow()
    window.setCentralWidget(FileSelector())
    window.show()
    app.exec()
