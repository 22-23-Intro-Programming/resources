# Piece Class
from graphics import *

class Piece:

    def __init__(self, pos, name, win):

        self.image = Circle(pos, 30)
        self.image.draw(win)
        self.name = name
        self.T = Text(pos, name)
        self.T.draw(win)

    def getName(self):
        return self.name

    def move(self):
        return False
