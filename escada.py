import turtle
t=turtle.Turtle()
t.shape("turtle")
ecra=turtle.getscreen()
t.left(90)
for i in range(5):
    t.forward(50)
    t.right()
ecra.mainloop()