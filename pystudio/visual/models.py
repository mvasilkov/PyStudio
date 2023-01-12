from __future__ import annotations
from typing import Literal

from pydantic import BaseModel


class QBoxLayoutStretchModel(BaseModel):
    'QBoxLayout::addStretch'
    type: Literal['QBoxLayoutStretch'] = 'QBoxLayoutStretch'
    stretch: int = 0


class QHBoxLayoutModel(BaseModel):
    type: Literal['QHBoxLayout'] = 'QHBoxLayout'
    name: str
    children: list[QBoxLayoutStretchModel | QVBoxLayoutModel | QLineEditModel | QPushButtonModel | QWidgetModel] = []


class QVBoxLayoutModel(BaseModel):
    type: Literal['QVBoxLayout'] = 'QVBoxLayout'
    name: str
    children: list[QBoxLayoutStretchModel | QHBoxLayoutModel | QLineEditModel | QPushButtonModel | QWidgetModel] = []


class QWidgetModel(BaseModel):
    type: Literal['QWidget'] = 'QWidget'
    name: str
    layout: QHBoxLayoutModel | QVBoxLayoutModel


class QPushButtonModel(BaseModel):
    type: Literal['QPushButton'] = 'QPushButton'
    name: str
    text: str


class QLineEditModel(BaseModel):
    type: Literal['QLineEdit'] = 'QLineEdit'
    name: str
    placeholderText: str = ''


for a in list(locals().values()):
    if isinstance(a, type) and issubclass(a, BaseModel):
        a.update_forward_refs()
