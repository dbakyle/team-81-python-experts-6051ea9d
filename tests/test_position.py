from unittest import TestCase
from levelup.position import Position

class TestPositionInitNoCoord(TestCase):
    def test_init(self):
        testobj = Position()
        self.assertEqual((0,0), testobj.getPosition())

class TestPositionInitWithCoord(TestCase):
    def test_init(self):
        testobj = Position(1,1)
        self.assertEqual((1,1), testobj.getPosition())
