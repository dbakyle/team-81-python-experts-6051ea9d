class Position:
    DEFAULT_X = 0
    DEFAULT_Y = 0
    x = DEFAULT_X
    y = DEFAULT_Y

    def __init__(self, x = DEFAULT_X, y = DEFAULT_Y):
        self.x = x
        self.y = y

    def getPosition(self):
        return self.x, self.y