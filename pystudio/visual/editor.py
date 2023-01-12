from PySide6.QtWidgets import QFrame, QHeaderView, QScrollArea, QSplitter, QTreeWidget, QVBoxLayout, QWidget

from .builder import Builder
from .poc.hello_dataclasses import hello


class VisualEditor(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        splitter = QSplitter()
        splitter.addWidget(StructurePane())

        scroll = QScrollArea()
        scroll.setFrameShape(QFrame.Shape.NoFrame)
        splitter.addWidget(scroll)

        # POC
        builder = Builder()
        widget = builder.build_widget(hello)
        scroll.setWidget(widget)
        widget.show()

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
        tree.setHeaderLabels(['Component'])
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
