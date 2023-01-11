from PySide6.QtGui import QPalette
from PySide6.QtWidgets import QFrame, QHeaderView, QScrollArea, QSplitter, QTreeWidget, QVBoxLayout, QWidget


class VisualEditor(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        splitter = QSplitter()
        splitter.addWidget(StructurePane())

        scroll = QScrollArea()
        scroll.setFrameShape(QFrame.Shape.NoFrame)
        scroll.setBackgroundRole(QPalette.ColorRole.Dark)
        splitter.addWidget(scroll)

        splitter.addWidget(PropertiesPane())
        splitter.setSizes([100, 300, 100])

        layout.addWidget(splitter)


class StructurePane(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        tree = QTreeWidget()
        tree.setMinimumWidth(100)
        tree.setHeaderLabels(['Component', ''])
        tree.header().setSectionsMovable(False)
        tree.header().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
        layout.addWidget(tree)


class PropertiesPane(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        tree = QTreeWidget()
        tree.setMinimumWidth(100)
        tree.setHeaderLabels(['Property', 'Value'])
        tree.header().setSectionsMovable(False)
        tree.header().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
        layout.addWidget(tree)
