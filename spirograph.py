import turtle as trtl
import random

t = trtl.Turtle()

t.speed(20)

x = 300
move_x = 25
colors = ["Royal blue", "deep sky blue", "cyan", "dark turquoise", "aquamarine", "cadet blue", "pale green"]

for i in range(9):
    x = x - move_x
    t.penup()
    t.fillcolor(random.choice(colors))
    t.begin_fill()
    t.goto(-x/2,x/2)
    t.pendown()
    for _ in range(4):
        t.forward(x - move_x)
        t.right(90)
    t.end_fill()

wn = trtl.Screen()
wn.mainloop()
