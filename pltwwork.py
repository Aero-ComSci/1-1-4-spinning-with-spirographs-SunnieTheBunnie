import turtle as trtl

painter = trtl.Turtle()
painter.penup()
painter.goto(-200, 0)
painter.pendown()

while True #used for step 19
  x = -200
  y = 0
  move_x = 1
  move_y = 1
  while (x < 200): #changed 0 to 200 for step 17
  
    while (y < 100):
      x = x + move_x
      y = y + move_y
      painter.goto(x,y)
    move_y = -1
    
    while (y > 0):
      x = x + move_x
      y = y + move_y
      painter.goto(x,y)
    move_y = 1
  
  painter.penup()
  painter.goto(200,0)
  painter.pendown()
  
  #start of step 18
  x = 200
  y = 0
  move_x = -1
  move_y = -1
  while (x > -200):
  
    while (y > -100):
      x = x + move_x
      y = y + move_y
      painter.goto(x,y)
    move_y = 1
    
    while (y < 0):
      x = x + move_x
      y = y + move_y
      painter.goto(x,y)
    move_y = -1


wn = trtl.Screen()
wn.mainloop()
