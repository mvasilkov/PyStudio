from .. import models

component = models.QWidgetModel(
    name='component',
    layout=models.QVBoxLayoutModel(
        name='vbox_layout',
        children=[
            models.QLineEditModel(
                name='line_edit1',
                placeholderText='Design GUI with Python',
            ),
            models.QLineEditModel(
                name='line_edit2',
                placeholderText='Python Bindings for Qt',
            ),
            models.QHBoxLayoutModel(
                name='hbox_layout',
                children=[
                    models.QBoxLayoutStretchModel(),
                    models.QPushButtonModel(
                        name='push_button1',
                        text='Qt for Python',
                    ),
                    models.QPushButtonModel(
                        name='push_button2',
                        text='PySide6',
                    ),
                ],
            ),
        ],
    ),
)
