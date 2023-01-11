from __future__ import annotations
from typing import Literal

from pydantic import BaseModel


class QHBoxLayoutModel(BaseModel):
    type: Literal['QHBoxLayout'] = 'QHBoxLayout'
    name: str
    children: list[QVBoxLayoutModel | QWidgetModel]


class QVBoxLayoutModel(BaseModel):
    type: Literal['QVBoxLayout'] = 'QVBoxLayout'
    name: str
    children: list[QHBoxLayoutModel | QWidgetModel]


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
    placeholderText: str
