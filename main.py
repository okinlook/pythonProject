from turtle import *

forward(50)
left(45)
forward(60)
left(30)
shape("turtle")
left(2000)
for i in range(125):
    forward(10)
    left(3)



forward(100)
left(90)
forward(100)
forward(50)
left(90)
forward(200)
left(90)
forward(250)
exitonclick
tvar = textinput("ahoj","co mam kreslit: ")
if tvar == "čtverec":
    for i in range(4):
        forward(100)
        left(90)

