from PySide6.QtWidgets import QHBoxLayout, QWidget


class VisualEditor(QWidget):
    def initialize(self):
        layout = QHBoxLayout(self)
        layout.addWidget(StructurePane())
        layout.addWidget(PropertiesPane())


class StructurePane(QWidget):
    def initialize(self):
        pass


class PropertiesPane(QWidget):
    def initialize(self):
        pass
