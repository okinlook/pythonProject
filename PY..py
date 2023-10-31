from turtle import *

def pismeno_a():
    forward(50)
    # tady nakresli zbytek
    penup() # ted to nekresli
    forward(0)  # posunu se o 50 a nekreslim
    pendown()  # ted zase zacnu kreslit
    right(90)
    forward(100)
    right(180)
    forward(100)
    left(90)
    forward(60)
    left(90)
    forward(100)
    right(180)
    forward(60)
    right(90)
    forward(60)
    right(90)
    forward(60)
    left(90)
def pismeno_x():
    penup()
    right(30)
    forward(60)
    right(90)
    pendown()
    forward(120)
    right(180)
    forward(60)
    right(120)
    forward(60)
    right(180)
    forward(120)
    right(180)
    forward(120)
    left(90)












pismeno_x ()
exitonclick()