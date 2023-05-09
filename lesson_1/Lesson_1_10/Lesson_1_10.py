# x = "maroqlidir"
# print ("Dasturlashni o'rganish"+x)

# set__data__type = {1, 2, 3, 5, 6, 8,}

# def SET(set__data: set, add__number: int ) -> set :
#     """
#         Bu setga ma'lumot qo'shish funksiyasi
#     """
#     set__data.add(add__number)

#     print(set__data)
    
# SET()
    
# set__data__type = {1, 2, 3, 5, 6, 8,}

# def SET(set__data: set, add__number: int ) -> set :
#     """
#         Bu setga ma'lumot qo'shish funksiyasi
#     """
#     if add__number in set__data:
#         print("Bu son mavjud.Siz boshqa son kiriting")
#     else:
#         print("Bu son mavjud emas.")
#         set__data.add(add__number)
#         print(set__data)
# SET(set__data__type, 5)

# set__data__type_1 = {3, 5, 7, 8, 9}
# set__data__type_2 = {1, 2, 4, 6}

# def SET(set__data_1: set, add__number_2: set) -> set:
#     """
#          Bu setga ma'lumot qo'shish funksiyasi
#     """
#     set__data__type_3 = set__data_1.union(add__number_2)
#     print(set__data__type_3)
# SET(set__data__type_1, set__data__type_2)

# x = "shirin"
# def funksiya():
#   x = "foydali"
#   print("Olma "+ x)
# funksiya()
# print ("Olma "+ x)


# def funksiya():
#     global x
#     x = "shirin"
#     print("Olma "+x)
# funksiya()
# print ("Olma "+x)


# x = "shirin"
# def funksiya():
#     global x
#     x = "foydali"
#     print("Olma "+ x)
# funksiya()
# print ("Olma "+ x)


# x = 5
# print(type(x))


# x = 1 #int
# y = 2.8 #float
# z = 1j #complex
# # int turidan floatga o'tkazish
# a = float(x)
# # float turidan intga o'tkazish
# b = int(x)
# # int turidan complexga o'tkazish
# c = complex(x)
# print(a)
# print(b)
# print(c)


# import random
# print (random.randrange(1,10))


# a = """ Bu
# ko'p qatorli
# satr """
# b = ''' Bu ham
# ko'p qatorli
# satr '''
# print(a)
# print(b)


# a = "Dasturlash"
# print(a[1])


# toq_son = {1, 3, 5, 7, 9}
# for x in toq_son:
#  print(x)
# # prin("---------\n")
# print(3 in toq_son)


# meva = {"nok", "banan", "shaftoli"}
# print(len(meva))


# x = {"a", "b", "c", "d"}
# y = {"g", "c", "e", "d"}
# z = x.difference(y)
# print(z)
# x.difference_update(y)
# print(x)


# x = {"a", "b", "c", "d"}
# y = {"g", "c", "e", "d"}
# z = x.intersection(y)
# print(z)
# x.intersection_update(y)
# print(x)


# x = {"a", "b", "c"}
# y = {"l", "m", "n", "o"}
# z = x.isdisjoint(y)
# print(z)


# x = {"a", "b", "c"}
# y = {"l", "m", "n", "o", "k", "q", "t", "b"}
# z = x.issubset(y)
# print(z)
# z = x.issuperset(y)
# print(x)


# x = {"a", "b", "c"}
# y = {"l", "c", "a", "o", "k", "t", "b"}
# z = x.symmetric_difference(y)
# print(z)
# z = x.symmetric_difference_update(y)
# print(x)


# meva = {"nok", "banan", "shaftoli"}
# x = meva.pop()
# print(meva)


# toq_son = {1, 3, 5, 7, 9}
# toq_son.add(9)
# print(toq_son)
# toq_son.update([11, 13, 15])
# print(toq_son)

# top ={
#     "name": "Kamoljon",
#     "surname": "Axmatov"
# }

# son = 12.0
# def funksiya(number: int) -> float:
#     str__number = str(number)
#     int__number = ""
#     for x in str__number:
#        if x != ".": int__number += x
#        else: break
#     int__number_2 = int(int__number)
#     print(int__number_2)
# funksiya(45.56)


# import datetime as dt
# x = dt.datetime.now()
# print(x)


# import datetime as dt
# x = dt.datetime.now()
# print(x.strftime("%B"))