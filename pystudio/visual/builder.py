from PySide6.QtWidgets import QHBoxLayout, QLineEdit, QPushButton, QVBoxLayout, QWidget


class Builder:
    def __init__(self):
        self.root = None
        self.components = {}

    def build_widget(self, model, *, save_root=True):
        method = getattr(self, f'_build_{model.type}', None)
        if method is None:
            raise ValueError(f'Unsupported model type: {model.type}')

        component = method(model)
        if hasattr(model, 'name'):
            component.setObjectName(model.name)
            self.components[model.name] = component

        if save_root:
            self.root = component
        return component

    def _build_QWidget(self, model):
        widget = QWidget()
        layout = self.build_widget(model.layout, save_root=False)
        widget.setLayout(layout)
        return widget

    def _build_QPushButton(self, model):
        button = QPushButton(model.text)
        return button

    def _build_QLineEdit(self, model):
        line_edit = QLineEdit()
        line_edit.setPlaceholderText(model.placeholderText)
        return line_edit

    def _build_QHBoxLayout(self, model):
        layout = QHBoxLayout()
        self._build_layout_children(model, layout)
        return layout

    def _build_QVBoxLayout(self, model):
        layout = QVBoxLayout()
        self._build_layout_children(model, layout)
        return layout

    def _build_layout_children(self, model, layout):
        for child in model.children:
            match child.type:
                case 'QBoxLayoutStretch':
                    layout.addStretch(child.stretch)

                case 'QHBoxLayout' | 'QVBoxLayout':
                    component = self.build_widget(child, save_root=False)
                    layout.addLayout(component)

                case _:
                    component = self.build_widget(child, save_root=False)
                    layout.addWidget(component)
