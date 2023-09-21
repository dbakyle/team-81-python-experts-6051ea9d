from unittest import TestCase
from levelup.map import Gamemap
from levelup.position import Position
class test_gamemap(TestCase):
    def test_init(self):
        testObj=Gamemap()
        startingposition=Position(0,0)
        testpos=testObj.calculateposition(startingposition,"NORTH")
        (x,y)=testpos.getPosition()
        assert x==0

    