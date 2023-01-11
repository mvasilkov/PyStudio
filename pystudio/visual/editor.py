from PySide6.QtGui import QPalette
from PySide6.QtWidgets import QFrame, QHBoxLayout, QScrollArea, QWidget


class VisualEditor(QWidget):
    def initialize(self):
        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(StructurePane().initialize())

        scroll = QScrollArea()
        scroll.setFrameShape(QFrame.Shape.NoFrame)
        scroll.setBackgroundRole(QPalette.ColorRole.Dark)
        layout.addWidget(scroll)

        layout.addWidget(PropertiesPane().initialize())

        return self


class StructurePane(QWidget):
    def initialize(self):
        self.setMinimumWidth(200)
        return self


class PropertiesPane(QWidget):
    def initialize(self):
        self.setMinimumWidth(200)
        return self
