from PySide6.QtWidgets import QApplication, QGraphicsView, QGraphicsScene, QGraphicsPixmapItem
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap

def fit_item_exactly(view: QGraphicsView, item: QGraphicsPixmapItem, aspect=Qt.KeepAspectRatio):
    """
    Scale and center the QGraphicsView so that `item` fills the viewport
    with no margin.
    """
    rect = item.sceneBoundingRect()
    if rect.isNull():
        return

    # Remove any existing scaling (rotation/shear is reset too)
    view.resetTransform()

    vp = view.viewport().rect()
    if vp.isEmpty():
        return

    sx = vp.width() / rect.width()
    sy = vp.height() / rect.height()

    # Maintain aspect ratio by default
    if aspect == Qt.KeepAspectRatio:
        s = min(sx, sy)
        view.scale(s, s)
    elif aspect == Qt.KeepAspectRatioByExpanding:
        s = max(sx, sy)
        view.scale(s, s)
    else:  # Qt.IgnoreAspectRatio
        view.scale(sx, sy)

    view.centerOn(rect.center())


if __name__ == "__main__":
    app = QApplication([])

    # Load your image
    pixmap = QPixmap("test_template.png")  # Replace with your image file

    # Build scene and view
    scene = QGraphicsScene()
    pixmap_item = QGraphicsPixmapItem(pixmap)
    scene.addItem(pixmap_item)

    view = QGraphicsView(scene)
    view.setFrameStyle(0)  # Remove view frame
    # view.setAlignment(Qt.AlignLeft | Qt.AlignTop)
    view.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
    view.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

    view.resize(600, 200)
    # fit_item_exactly(view, pixmap_item)  # Fit the pixmap without margins

    view.show()
    view.fitInView(pixmap_item, Qt.KeepAspectRatio)
    app.exec()
