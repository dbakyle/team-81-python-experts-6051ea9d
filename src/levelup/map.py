from levelup.position import Position

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

    def newposition(self,checkposition,Direction,move):
            (x,y) = checkposition.getPosition()
            retval = True
            if Direction == North:
                North = y++1
            if Direction == West:
                West == x--1
            if Direction == East:
                East = x++1
            if Direction == South:
                South = y--1


         