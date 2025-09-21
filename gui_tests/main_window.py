import sys

from PySide6.QtCore import QSize
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QSizePolicy

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
        self.controls_panel.checkbox.stateChanged.connect(self.template_viewer.show_dummy_code)
        self.hlayout.addWidget(self.controls_panel)

        self.central_widget = QWidget()
        self.central_widget.setLayout(self.hlayout)
        self.setCentralWidget(self.central_widget)

        # self.template_viewer.setFixedSize(self.template_viewer.size())
        # print(self.template_viewer.size())


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
    # sys.exit(app.exec())

    print("HOLA")
    print(window.template_viewer.size())
    print(window.template_viewer.scaled_pixmap.size())
    print(window.template_viewer.image_label.size())
