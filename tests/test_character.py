from unittest import TestCase
from unittest.mock import MagicMock, create_autospec
from levelup.character import Character

# All the unit tests for the Character should go here
# Unit tests for other classes should be in their own .py files (like test_character.py)
class TestCharacter(TestCase):
    def test_init(self):
        testObj = Character()