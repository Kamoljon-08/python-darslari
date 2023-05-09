# import turtle as t
# x = t.getscreen()
# x.setup(800,800)
# x.bgcolor("white")

# for i in range(20):
#     t.color("red")
#     t.fd(2+2*i)
#     t.left(45)
# t.reset()

# t.color("red")
# t.penup() 
# t.sety(0) 
# t.pendown() 
# t.color('pink') 
# t.begin_fill() 
# t.circle(150) 
# t.end_fill() 
# t.penup() 
# t.sety(50) 
# t.pendown() 
# t.color('yellow') 
# t.begin_fill() 
# t.circle(100) 
# t.end_fill() 
# t.penup() 
# t.sety(-5) 
# t.pendown() 
# t.color('green') 
# t.width(10) 
# t.right(90) 
# t.forward(150) 
# t.backward(50) 
# t.fillcolor('chartreuse') 
# t.begin_fill() 
# t.left(120) 
# t.forward(75) 
# t.left(150) 
# t.forward(60) 
# t.end_fill() 
# t.penup() 
# t.fillcolor('chartreuse') 
# t.begin_fill() 
# t.forward(10) 
# t.pendown() 
# t.forward(60) 
# t.left(150) 
# t.forward(75) 
# t.end_fill()
# t.resetscreen()

#########################################################################################

# t.color("red")
# t.penup() 
# t.sety(0) 
# t.pendown() 
# t.color('pink') 
# t.begin_fill() 
# t.circle(150) 
# t.end_fill() 
# t.penup() 
# t.sety(50) 
# t.pendown() 
# t.color('yellow') 
# t.begin_fill() 
# t.circle(100) 
# t.end_fill() 
# t.penup() 
# t.sety(-5) 
# t.pendown() 
# t.color('green') 
# t.width(10) 
# t.right(90) 
# t.forward(150) 
# t.backward(50) 
# t.fillcolor('chartreuse') 
# t.begin_fill() 
# t.left(120) 
# t.forward(75) 
# t.left(150) 
# t.forward(60) 
# t.end_fill() 
# t.penup() 
# t.fillcolor('chartreuse') 
# t.begin_fill() 
# t.forward(10) 
# t.pendown() 
# t.forward(60) 
# t.left(150) 
# t.forward(75) 
# t.end_fill()
# t.reset()

# mainloop()

###########################################################################################

import turtle as t

x = t.getscreen()
x.setup(800,800)
x.bgcolor("white")

# sc = t.Screen()
# sc.setup(800, 800)
# print(t.window_height())
# print(t.window_width())

# sc = t.Screen()
# sc.setup(400, 400, startx = 50, starty = -200)

# i = t.textinput('Log out', 'User name')
# print(i)

# t.numinput('Log out','number fon', 9)

# num = int(t.numinput("Control Detail", "Phone no.", default = 9999999999, minval = 6000000000, maxval = 9999999999))
# print(num)

# num = int(t.numinput("Control Detail", "Phone no."))
# print(num)

# t.circle(100)
# tur2 = t.Turtle()
# tur2 = t.clone()
# tur2.circle(-100)

# for i in range(60):
#     t.delay(60)
#     t.fd(50 * 60 * i)


i = t.textinput('Log out', 'User name')
print('My name is', i)

x = t.textinput('Log out', 'User age')
print('I turned', x, 'today')

v = 'Congratulations on your 15th birthday'
print(v)

w = 'Happy Brithday'
print(w)
    

t.mainloop()