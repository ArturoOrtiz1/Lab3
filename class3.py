from graphics import *
def main():
        win=GraphWin()
        shape=Rectangle(Point(10,30),Point(40,70))
        shape.setOutline("red")
        shape.setFill("red")
        shape.draw(win)
        for i in range(10):
                p=win.getMouse()
                cornerPoint=shape.getP1()
                c=shape.getCenter()
                dx=p.getX()-c.getX()
                dy=p.getY()-c.getY()
                shape.move(dx,dy)
        win.close()

main()
