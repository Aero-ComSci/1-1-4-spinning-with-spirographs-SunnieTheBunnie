import turtle as trtl

t = trtl.Turtle()

t.speed(20)

x = 10
move_x = 40

for i in range(9):
    x = x + move_x
    t.penup()
    t.goto(-x/2,x/2)
    t.pendown()
    for _ in range(4):
        t.forward(x + move_x)
        t.right(90)

wn = trtl.Screen()
wn.mainloop()
