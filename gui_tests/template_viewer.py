from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QPixmap, QPalette, QColor
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QFrame, QGraphicsScene, QGraphicsView, QGraphicsItem

from PySide6.QtWidgets import QGraphicsView, QGraphicsPixmapItem
from PySide6.QtCore import QRectF, Qt

from color_widget import ColorWidget
from pathlib import Path
PROJECT_ROOT: Path = Path(__file__).resolve().parents[1]
DATA_DIR: Path = PROJECT_ROOT / "data"
TEMPLATE_DIR: Path = DATA_DIR / "template.png"
DUMMY_DIR: Path = DATA_DIR / "dummy.png"


class TemplateViewer(QWidget):
    def __init__(self):
        super().__init__()

        self.vlayout = QVBoxLayout()
        self.vlayout.setContentsMargins(0, 0, 0, 0)
        self.vlayout.setAlignment(Qt.AlignCenter)  # Center the label

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(220, 220, 220))
        self.setPalette(palette)
        self.setAutoFillBackground(True)

        self.image_label = QLabel()
        self.image_label.setAlignment(Qt.AlignCenter)
        self.vlayout.addWidget(self.image_label)



        self.setLayout(self.vlayout)

    def display_template(self, file_path):
        self.pixmap = QPixmap(file_path)
        self.scaled_pixmap = self.pixmap.scaled(
            self.size(),
            aspectMode=Qt.KeepAspectRatio,
            mode=Qt.SmoothTransformation
        )

        self.image_label.setPixmap(self.scaled_pixmap)
        self.image_label.setFixedSize(self.scaled_pixmap.size())
        self.image_label.setFrameShape(QFrame.Box)
    
    def show_dummy_code(self, state):
        pass










# class TemplateViewer(QWidget):
#     def __init__(self):
#         super().__init__()

#         self.setFixedSize(QSize(300, 400))

#         self.vlayout = QVBoxLayout()
#         self.vlayout.setContentsMargins(0, 0, 0, 0)

#         self.scene = QGraphicsScene()
#         self.view = QGraphicsView(self.scene)

#         self.vlayout.addWidget(self.view)
#         self.setLayout(self.vlayout)
    
#     def display_template(self, file_path):
#         self.pixmap = QPixmap(file_path)        
#         self.pixmapitem = self.scene.addPixmap(self.pixmap)
#         self.pixmapitem.setTransformationMode(Qt.SmoothTransformation)
#         self.view.fitInView(self.pixmapitem, Qt.KeepAspectRatio)

#     def show_dummy_code(self, state):
#         if state == 2:
#             self.pixmap2 = QPixmap(DUMMY_DIR)
#             self.pixmapitem2 = self.scene.addPixmap(self.pixmap2)
#             self.pixmapitem2.setTransformationMode(Qt.SmoothTransformation)
#             self.pixmapitem2.setFlags(QGraphicsItem.ItemIsMovable | QGraphicsItem.ItemIsSelectable)
#         else:
#             self.scene.removeItem(self.pixmapitem2)
