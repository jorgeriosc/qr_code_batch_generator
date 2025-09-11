import sys

from PySide6.QtCore import QSize
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout

from controls_panel import ControlsPanel
from template_viewer import TemplateViewer


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QR Expo")
        self.resize(QSize(800, 600))

        self.hlayout = QHBoxLayout()

        self.template_viewer = TemplateViewer()
        self.hlayout.addWidget(self.template_viewer)

        self.controls_panel = ControlsPanel()
        self.controls_panel.file_selector.file_selected.connect(self.template_viewer.display_template)
        self.hlayout.addWidget(self.controls_panel)

        dummy_widget = QWidget()
        dummy_widget.setLayout(self.hlayout)
        self.setCentralWidget(dummy_widget)


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
