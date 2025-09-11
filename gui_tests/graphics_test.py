import sys

from PySide6.QtWidgets import QApplication, QGraphicsScene, QGraphicsView, QGraphicsPixmapItem
from PySide6.QtGui import QPixmap, QImage, QPainter
from PySide6.QtCore import Qt

from pathlib import Path
template_path = Path(__file__).resolve().parents[1] / "data" / "template.png"

app = QApplication([])

# Load as QImage to avoid device-dependent scaling issues
image = QImage(template_path)
pixmap = QPixmap.fromImage(image)

scene = QGraphicsScene()
item = QGraphicsPixmapItem(pixmap)
scene.addItem(item)
scene.setSceneRect(pixmap.rect())

view = QGraphicsView(scene)
view.setRenderHints(view.renderHints() | 
                    QPainter.SmoothPixmapTransform | 
                    QPainter.Antialiasing)

# Ensure 1:1 pixels, no automatic scaling
view.resetTransform()
view.setTransformationAnchor(QGraphicsView.NoAnchor)
view.setResizeAnchor(QGraphicsView.NoAnchor)
view.setViewportUpdateMode(QGraphicsView.FullViewportUpdate)

view.show()
app.exec()



