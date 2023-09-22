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
    
    def newposition(self):
        North=(x,y++1)
        East=(x++1,y)
        West=(x--1,y)
        South=(x,y--1)
        


    
    