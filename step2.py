import turtle as trtl

screen = trtl.Screen()
screen.setup(width=800)

#red circle object
t = trtl.Turtle()
t.shape("circle")
t.color("red")
t.penup()

#number of circles drawn and radius of the circle
circles = 5
circle_radius = 40

#total circle diameter, spacing calculation using screen width, amount of space in between each circle
circle_length = circle_radius*2
spacing = screen.window_width() - circle_length
spaceinbetween = spacing / (circles + 1) 

#starting position based on circle length and space in between the objects
x = -screen.window_width() / 2 + spaceinbetween + circle_radius / 2
y = 0

#repeating the positioning of the circles 5 times, evenly
for i in range(circles):
    t.goto(x + i * (circle_radius + spaceinbetween), y)
    t.stamp() 

wn = trtl.Screen()
wn.mainloop()
