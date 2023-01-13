from PySide6.QtWidgets import (
    QFrame,
    QHeaderView,
    QScrollArea,
    QSplitter,
    QTreeWidget,
    QTreeWidgetItem,
    QVBoxLayout,
    QWidget,
)

from .builder import Builder
from .poc.hello_dataclasses import hello


class VisualEditor(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        splitter = QSplitter()
        splitter.addWidget(StructurePane(hello))

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
    def __init__(self, model, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.model = model

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        tree = QTreeWidget()
        tree.setMinimumWidth(100)
        tree.setHeaderLabels(['Component', 'Type'])
        tree.header().setSectionsMovable(False)
        tree.header().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
        tree.addTopLevelItem(self.loadModel(model))
        layout.addWidget(tree)

    def loadModel(self, model, parent=None):
        if model.type == 'QBoxLayoutStretch':
            props = ['(stretch)', '']
        else:
            props = [model.name, model.type]

        entry = QTreeWidgetItem(props)
        if parent is not None:
            parent.addChild(entry)

        match model.type:
            case 'QWidget':
                self.loadModel(model.layout, entry)

            case 'QHBoxLayout' | 'QVBoxLayout':
                for child in model.children:
                    self.loadModel(child, entry)

        return entry


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
