"""

    round() -> nuqtadan keyingi soni olish
    ceil(x)- x ga teng yoki katta eng kichik butun son.
    floor(x)- x ga teng yoki kichik eng katta butun son
    fmod(x,y)- x ni y ga bo`lgandagi qoldiq qism.
    factorial(x)- x ning faktoriali. N!=1*2*3*…*n
    pi-pi konstantasi
    pow(x,y)- x**y
    sqrt(z)- z ning kvadrat ildizi.
    trunc(x)- x haqiqiy sonning butun qismini qaytaradi

    1 * 2 * 3 * 4 * 5
"""


"""
    inputdan a soni olasiz

        shunu a^4 bunda 2 ta koptiruvchi amal bo'lishi kerak
        shunu a^6 bunda 3 ta 
        shunu a^15 bunda 5 ta




"""

son = int(input("Son kiriting: "))

# a = 0
# a = son * son
# print(a * a)

# a = 0
# a = son * son
# print(a * a * a)

a = 0
b = 0
c = 0
a = son * son * son
b = a * a
c = b * b * a
print(c)
# 32768

import math

# # nuqtadan keyingi soni olish
# print(round(13.5678798, 3))

# # x ga teng yoki katta eng kichik butun son
# x = math.ceil(23.67)
# print(x)

# # i ga teng yoki kichik eng katta butun son
# i = math.floor(23.6778)
# print(i)

# # i ni y ga bo`lgandagi qoldiq qism
# a = math.fmod(12, 5)
# print(a)

# # x**y daraga ko'tarib beradi
# print(pow(3, 5))

# # z ning kvadrat ildizi
# z = math.sqrt(25)
# print(z)

# # v haqiqiy sonning butun qismini qaytaradi
# v = math.trunc(12.4567)
# print(v)

# # n ning faktoriali. N!=1*2*3*…*n
# n = math.factorial(1*2*3)
# print(n)

# # konstantasi
# m = math.pi
# print(m)


# number = int(input("Son kirting: "))
# count = 1
# for i in range(1, number + 1):
#     count *= i
    
# print(math.factorial(5))

# print(count)