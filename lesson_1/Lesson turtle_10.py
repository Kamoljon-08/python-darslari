# import turtle
# import random

# p_one = turtle.Turtle()
# p_one.color("purple")
# p_one.shape("turtle")
# p_one.penup()
# p_one.goto(-300,100)
# p_two = p_one.clone()
# p_two.color("orange")
# p_two.penup()
# p_two.goto(-300,-100)

# p_one.goto(300,60)
# p_one.pendown()
# p_one.circle(40)
# p_one.penup()
# p_one.goto(-200,100)
# p_two.goto(300,-140)
# p_two.pendown()
# p_two.circle(40)
# p_two.penup()
# p_two.goto(-200,-100)


# p_one.goto(210,60)
# p_one.pendown()
# p_one.circle(40)
# p_one.penup()
# p_one.goto(-200,100)
# p_two.goto(210,-140)
# p_two.pendown()
# p_two.circle(40)
# p_two.penup()
# p_two.goto(-200,-100)


# p_one.goto(120,60)
# p_one.pendown()
# p_one.circle(40)
# p_one.penup()
# p_one.goto(-200,100)
# p_two.goto(120,-140)
# p_two.pendown()
# p_two.circle(40)
# p_two.penup()
# p_two.goto(-200,-100)


# p_one.goto(30,60)
# p_one.pendown()
# p_one.circle(40)
# p_one.penup()
# p_one.goto(-200,100)
# p_two.goto(30,-140)
# p_two.pendown()
# p_two.circle(40)
# p_two.penup()
# p_two.goto(-200,-100)


# p_one.goto(-60,60)
# p_one.pendown()
# p_one.circle(40)
# p_one.penup()
# p_one.goto(-200,100)
# p_two.goto(-60,-140)
# p_two.pendown()
# p_two.circle(40)
# p_two.penup()
# p_two.goto(-200,-100)

# die = [1,2,3,4,5,6]
# for i in range(20):
#     if p_one.pos() >= (300,100):
#             print("Birinchi o'yinchi g'alaba qozonadi!")
#             break
#     elif p_two.pos() >= (300,-100):
#             print("Ikki o'yinchi g'alaba qozondi!")
#             break
#     else:
#             p_one_turn = input("Qatlamni aylantirish uchun 'Enter' tugmasini bosing ")
#             die_outcome = random.choice(die)
#             print("Kalip rulosining natijasi: ")
#             print(die_outcome)
#             print("Qadamlar soni bo'ladi: ")
#             print(20*die_outcome)
#             p_one.fd(20*die_outcome)
#             p_two_turn = input("Qatlamni aylantirish uchun 'Enter' tugmasini bosing ")
#             die_outcome = random.choice(die)
#             print("Kalip rulosining natijasi: ")
#             print(die_outcome)
#             print("Qadamlar soni bo'ladi: ")
#             print(20*die_outcome)
#             p_two.fd(20*die_outcome)

 
from turtle import *
from random import randint

fd(100)
write(0)
fd(100)
write(5)
write(0)
fd(20)
write(1)
fd(20)
write(2)
fd(20)
write(3)
fd(20)
write(4)
fd(20)
write(5)
fd(20)

for step in range(5):
        write(step)
        fd(20)

for step in range(6):
        write(step)
        fd(20)

goto(-140, 140)
for step in range(6):
        write(step)
        fd(20)

penup()
goto(-140, 140)

for step in range(6):
        write(step)
        fd(20)

for step in range(6):
        write(step)
        right(90)
        fd(10)
        pendown()
        fd(150)
        penup()
        backward(160)
        left(90)
        fd(20)

for step in range(6):
        write(step, align = 'center')
        right(90)
        fd(10)
        pendown()
        fd(150)
        penup()
        backward(160)
        left(90)
        fd(20)

speed(10)
penup()
goto(-140, 140)

ada = Turtle()
ada.color("red")
ada.shape("turtle")

ada = Turtle()
ada.color("red")
ada.shape("turtle")

ada.penup()
ada.goto(-160, 100)
ada.pendown()

ada.penup()
ada.goto(-160, 100)
ada.pendown()

for turn in range(100):
        ada.fd(randint(1, 5))

bob = Turtle()
bob.color("blue")
bob.shape("turtle")

bob.penup()
bob.goto(-160, 70)
bob.pendown()

for turn in range(100):
        ada.fd(randint(1, 5))
        bob.fd(randint(1, 5))

log = Turtle()
log.color("green")
log.shape("turtle")

log.penup()
log.goto(-160, 40)
log.pendown()

for turn in range(100):
        ada.fd(randint(1, 5))
        bob.fd(randint(1, 5))
        log.fd(randint(1, 5))

mainloop()