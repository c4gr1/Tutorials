import turtle

t = turtle.Turtle()

def kareCiz(uzunluk) :    
    for i in range(4) :
        t.forward(uzunluk)
        t.right(90)

def ucgenCiz(uzunluk):
    for a in range(3) :   
        t.forward(uzunluk)
        t.left(120)


for i in range(3):
    kareCiz(50)
    t.forward(50)

t.penup()
t.back(300)
t.pendown()
kareCiz(100)
t.penup()
t.back(150)
t.right(90)
t.forward(100)
t.left(90)
t.pendown()
ucgenCiz(100)

turtle.done()

