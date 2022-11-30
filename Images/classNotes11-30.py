from graphics import *
from Button import *


def fixGrayScale(img):

    x = img.getWidth()
    y = img.getHeight()
    print(x)
    print(y)

    for i in range(x):
        for j in range(y):
            p = img.getPixel(i, j)
            r, g, b = p[0], p[1], p[2]
            if ((r == g) and (r == b)):
                c = color_rgb(255, 255, 255)
                img.setPixel(i, j, c)
    

def main():

    win = GraphWin("Image Example", 800, 600)

    win.setBackground('#FF77FF')

    ball = Image(Point(350,500), "soccerball.png")
    ball.draw(win)

    pul = Image(Point(600, 350), "pulisic.png")
    pul.draw(win)

    fixGrayScale(pul)


if __name__ == "__main__":
    main()
