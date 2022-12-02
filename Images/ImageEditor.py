from graphics import*
from Button import*

def darken(img):

    x = img.getWidth()
    y = img.getHeight()

    for i in range(x):
        for j in range(y):
            pix = img.getPixel(i, j)
            r, g, b = pix[0], pix[1], pix[2]
            newColor = color_rgb(abs(r - 50), abs(g - 50), abs(b - 50))
            img.setPixel(i, j, newColor)
    

def main():

    win = GraphWin("Image Editor", 800, 600)
    win.setBackground("#FFAA00")

    I = Image(Point(300, 300), "veitchii.png")
    I.draw(win)

    B = Button(win, Point(600, 100), Point(700, 175), "tomato", "Darken")
    B2 = Button(win, Point(600, 200), Point(700, 275), "tomato", "Lighten")

    Q = Button(win, Point(600, 300), Point(700, 375), "misty rose", "QUIT")

    while True:
        m = win.getMouse()
        
        if B.isClicked(m):
            darken(I)
            
        #if B2.isClicked(m):

        if Q.isClicked(m):
            break

    win.close()

if __name__ == "__main__":
    main()
