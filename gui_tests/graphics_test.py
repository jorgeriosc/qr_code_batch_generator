import sys
from pathlib import Path
from template_viewer import TemplateViewer

from PySide6.QtCore import QPointF, Qt, QSize
from PySide6.QtGui import QBrush, QPainter, QPen, QPixmap, QPolygonF
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QHBoxLayout,
    QLabel,
    QGraphicsItem,
    QGraphicsScene,
    QGraphicsView,
)


PROJECT_ROOT: Path = Path(__file__).resolve().parents[1]
DATA_DIR: Path = PROJECT_ROOT / "data"
TEMPLATE_DIR: Path = DATA_DIR / "template.png"
DUMMY_DIR: Path = DATA_DIR / "dummy.png"


class TemplateViewerTest(QWidget):
    def __init__(self):
        super().__init__()

        self.vlayout = QHBoxLayout()
        self.vlayout.setContentsMargins(0, 0, 0, 0)

        self.image_label = QLabel()
        self.vlayout.addWidget(self.image_label)

        self.setLayout(self.vlayout)

    def display_template(self, file_path):
        pixmap = QPixmap(file_path)
        pixmap = pixmap.scaled(
            self.image_label.size(),
            aspectMode=Qt.KeepAspectRatio,
            mode=Qt.SmoothTransformation
        )

        self.image_label.setPixmap(pixmap)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Image Viewer Test")
        self.resize(QSize(800, 600))

        self.hlayout = QHBoxLayout()

        # self.template_viewer = TemplateViewer()
        # self.template_viewer.display_template(TEMPLATE_DIR)
        # self.hlayout.addWidget(self.template_viewer)

        
        self.scene = QGraphicsScene()
        self.pixmap = QPixmap(TEMPLATE_DIR)
        self.pixmapitem = self.scene.addPixmap(self.pixmap)

        print(type(self.pixmapitem))
        self.pixmapitem.setFlags(QGraphicsItem.ItemIsMovable | QGraphicsItem.ItemIsSelectable)
        self.pixmapitem.setTransformationMode(Qt.SmoothTransformation)

        # self.template_viewer2 = TemplateViewerTest()
        # self.template_viewer2.display_template(TEMPLATE_DIR)
        # self.template_viewer2_item = self.scene.addWidget(self.template_viewer2)

        # print(type(self.template_viewer2_item))

        # self.template_viewer2_item.setFlags(QGraphicsItem.ItemIsMovable | QGraphicsItem.ItemIsSelectable)

        self.view = QGraphicsView(self.scene)
        self.view.setRenderHint(QPainter.Antialiasing)
        self.hlayout.addWidget(self.view)


        dummy_widget = QWidget()
        dummy_widget.setLayout(self.hlayout)
        self.setCentralWidget(dummy_widget)






def main():
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


    # scene = QGraphicsScene(0, 0, 400, 200)


    # pixmap = QPixmap(TEMPLATE_DIR)
    # pixmapitem = scene.addPixmap(pixmap)

    # view = QGraphicsView(scene)
    # view.setRenderHint(QPainter.Antialiasing)
    # view.show()

    # app.exec()


if __name__ == "__main__":
    main()