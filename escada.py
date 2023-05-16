import turtle
t=turtle.Turtle()
t.shape("turtle")
ecra=turtle.getscreen()
t.left(90)
for i in range(10):
    if i % 2==0:
        t.right(90)
        t.forward(50)
    if i % 2 !=0:
        t.left(90)
        t.forward(50)
ecra.mainloop
