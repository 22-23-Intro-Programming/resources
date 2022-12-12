# Square Class
from graphics import *
from Piece import *

class Square:

    def __init__(self, pos, win):

        self.pieceExist = False
        self.r = Rectangle(pos, Point(pos.getX() + 80, pos.getY() + 80))
        self.r.draw(win)
        self.piece = None
        self.pos = pos

    def getPos(self):
        return self.pos

    def hasPiece(self):
        return self.pieceExist

    def getPiece(self):
        return self.piece

    def addPiece(self, piece):
        self.piece = piece
        self.pieceExist = True

    def removePiece(self):
        self.piece = None
        self.pieceExist = False


def main():

    win = GraphWin("Chess Testing", 1000, 800)

    squares = []    
    for i in range(8):
        row = []
        for j in range(8):
            row.append(Square(Point(100 + 80*i, 100 + 80*j), win))
        squares.append(row)

    #print(squares)

    k1 = Piece(Point(220, 220), "knight", win)
    squares[1][1].addPiece(k1)

    for i in range(8):
        for j in range(8):
            print(squares[i][j].getPos())
            if squares[i][j].hasPiece():
                print(squares[i][j].getPiece().getName())

if __name__ == "__main__":
    main()



    
