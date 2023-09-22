from levelup.position import Position
from levelup.controller import Direction

class Gamemap:
    def __init__(self):
        pass
    def calculateposition(self,startingposition,Direction):
        (x,y)=startingposition.getPosition()
        newposition=Position(x,y)
        return newposition

    def validateposition(self, checkposition):
        (x,y) = checkposition.getPosition()
        retval = True
        if x < 0 or x >= 10:
            retval = False
        if y < 0 or y >= 10:
            retval = False
        return retval

    def calculateposition(self,checkposition,move):
            (x,y) = checkposition.getPosition()
            
            if move == Direction.NORTH:
                y=y+1
            if move == Direction.WEST:
                x=x-1
            if move == Direction.EAST:
                x=x+1
            if move == Direction.SOUTH:
                y=y-1

            newpos=Position(x,y)
            return newpos


         