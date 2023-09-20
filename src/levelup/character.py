import logging
from dataclasses import dataclass
from enum import Enum

DEFAULT_NAME = "Bob"

class Character:
    def __init__(self, character_name = DEFAULT_NAME):
        self.name = character_name