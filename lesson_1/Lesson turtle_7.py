# import turtle as t
# x = t.getscreen()
# x.setup(800,800)
# x.bgcolor("black") 
 
# t.color("blue")
# t.left(60) 
# t.forward(200) 
# t.left(120) 
# t.forward(200) 
# t.left(120) 
# t.forward(200) 
# t.left(150) 

# t.forward(174) 
# t.backward(174) 
# t.left(16.5) 
# t.forward(180) 
# t.backward(180) 
# t.right(31.5) 
# t.forward(180) 
# t.right(75) 

# t.forward(53) 
# t.left(120) 
# t.forward(50) 
# t.left(120) 
# t.forward(50) 
 
# t.right(120) 
# t.forward(50) 
# t.left(120) 
# t.forward(50) 
     
# t.right(120) 
# t.forward(50) 
# t.left(120) 
# t.forward(50) 
 
# t.right(120) 
# t.forward(50) 
# t.left(120) 
# t.forward(50) 
# t.left(180) 
# t.forward(50) 
 
# t.left(300) 
# t.forward(160)

# t.mainloop()

        # *****************************************************************************

# import time 
# import datetime as dt 
# import turtle 

# t = turtle.Turtle() 
# t1 = turtle.Turtle() 
# s = turtle.Screen() 
# s.bgcolor("green") 

# sec = dt.datetime.now().second 
# min = dt.datetime.now().minute 
# hr = dt.datetime.now().hour 
# t1.pensize(3) 
# t1.color('black') 
# t1.penup() 
# t1.goto(-20, 0) 
# t1.pendown() 

# for i in range(2): 
#         t1.forward(200) 
#         t1.left(90) 
#         t1.forward(70) 
#         t1.left(90)  
# t1.hideturtle() 
# while True: 
#         t.hideturtle() 
#         t.clear() 

#         t.write(str(hr).zfill(2) 
#         + ":"+str(min).zfill(2)+":" 
#         + str(sec).zfill(2), 
#         font=("Arial Narrow", 35, "bold")) 
#         time.sleep(1) 
#         sec += 1 
#         if sec == 60: 
#                 sec = 0 
#                 min += 1 
#         if min == 60: 
#                 min = 0 
#                 hr += 1 
#         if hr == 13: 
#                 hr = 1

                # ******************************************************************

# import turtle as t
# x = t.getscreen()
# x.setup(800,800)
# x.bgcolor("sky blue") 

# def draw_circle(color, radius, x, y): 
#         t.penup() 
#         t.fillcolor (color) 
#         t.goto (x, y) 
#         t.pendown() 
#         t.begin_fill() 
#         t.circle (radius) 
#         t.end_fill() 
 
# draw_circle ("#ffffff", 30, 0, -40) 
# draw_circle ("#ffffff", 40, 0, -100) 
# draw_circle ("#ffffff", 60, 0, -200) 
# draw_circle ("#ffffff", 2, -10, -10) 
# draw_circle ("#ffffff", 2, 10, -10)  
# draw_circle ("#FF6600", 3, 0, -15) 
# draw_circle ("#ffffff", 2, 0, -35) 
# draw_circle ("#ffffff", 2, 0, -45) 
# draw_circle ("#ffffff", 2, 0, -55) 
 
# def create_line(x, y, length, angle): 
#         t.penup() 
#         t.goto(x, y) 
#         t.setheading(angle) 
#         t.pendown() 
#         t.forward(length) 
#         t.setheading(angle + 20) 
#         t.forward(20) 
#         t.penup() 
#         t.back(20) 
#         t.pendown() 
#         t.setheading(angle - 20) 
#         t.forward(20) 
#         t.penup() 
#         t.home() 
  
# create_line(-70, -50, 50, 160) 
# create_line(70, -50, 50, 20)

# t.mainloop()

                # **************************************************

# import turtle 
 
 
# # Screen() method to get screen 
# wn=turtle.Screen() 
 
# # creating tess object 
# tess=turtle.Turtle() 
 
 
# def triangle(x,y): 
 
#  # it is used to draw out the pen 
#  tess.penup() 
  
#  # it is used to move cursor at x 
#  # and y position 
#  tess.goto(x,y) 
  
#  # it is used to draw in the pen 
#  tess.pendown() 
#  for i in range(3): 
  
#   # move cursor 100 unit 
#   # digit forward 
#   tess.forward(100) 
   
#   # turn cursor 120 degree left 
#   tess.left(120) 
   
#   # Again,move cursor 100 unit 
#   # digit forward 
#   tess.forward(100) 
   
# # special built in function to send current 
# # position of cursor to triangle 
# turtle.onscreenclick(triangle,1) 
 
# turtle.listen() 
 
# # hold the screen 
# turtle.done()

                # *************************************************************************

# # Import required module 
# import turtle 
 
# # Create turtle object 
# t = turtle.Turtle() 
 
# # Create a screen 
# screen =turtle.Screen() 
 
# # Set background color 
# screen.bgcolor("sky blue") 
 
 
 
# # Function to draw body of snowman 
# def draw_circle(color, radius, x, y): 
#  t.penup() 
#  t.fillcolor (color) 
#  t.goto (x, y) 
#  t.pendown() 
#  t.begin_fill() 
#  t.circle (radius) 
#  t.end_fill() 
 
 
  
# # Illustrating snowman 
# # Drawing snowman body 
# draw_circle ("#ffffff", 30, 0, -40) 
# draw_circle ("#ffffff", 40, 0, -100) 
# draw_circle ("#ffffff", 60, 0, -200) 
 
# # Drawing left eye 
# draw_circle ("#ffffff", 2, -10, -10) 
 
# # Drawing right eye 
# draw_circle ("#ffffff", 2, 10, -10) 
 
# # Drawing nose 
# draw_circle ("#FF6600", 3, 0, -15) 
 
# # Drawing buttons on 
# draw_circle ("#ffffff", 2, 0, -35) 
# draw_circle ("#ffffff", 2, 0, -45) 
# draw_circle ("#ffffff", 2, 0, -55) 
 
 
 
# # Function to draw arms 
# def create_line(x, y, length, angle): 
#  t.penup() 
#  t.goto(x, y) 
#  t.setheading(angle) 
#  t.pendown() 
#  t.forward(length) 
#  t.setheading(angle + 20) 
#  t.forward(20) 
#  t.penup() 
#  t.back(20) 
#  t.pendown() 
#  t.setheading(angle - 20) 
#  t.forward(20) 
#  t.penup() 
#  t.home() 
  
 
  
# # Drawing left arm 
# create_line(-70, -50, 50, 160) 
 
# # Drawing right arm 
# create_line(70, -50, 50, 20) 
 
 
 
# # Drawing hat 
# t.penup() 
# t.goto (-35, '😍') 
# t.color ("black") 
# t.pensize (6) 
# t.pendown() 
# t.goto (35, '😍') 
 
# t.goto (30, '😍') 
# t.fillcolor ("black") 
# t.begin_fill() 
# t.left (90) 
# t.forward (15) 
# t.left (90) 
# t.forward (60) 
# t.left (90) 
# t.forward (15) 
# t.end_fill()

# t.mainloop()