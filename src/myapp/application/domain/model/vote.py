"""
Model for a vote in the application.
"""
from enum import Enum


class Vote(Enum):
    UP = 'up'
    DOWN = 'down'
