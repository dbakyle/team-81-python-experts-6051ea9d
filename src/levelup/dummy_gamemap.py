class Gamemap:
    def __init__(self):
        pass

    def calculatenewposition(self,startingPos, direction):
        return startingPos

    def validateposition(self, checkposition):
        (x,y) = checkposition.getPosition()
        retval = True
        if x < 0 or x >= 10:
            retval = False
        if y < 0 or y >= 10:
            retval = False
        return retval