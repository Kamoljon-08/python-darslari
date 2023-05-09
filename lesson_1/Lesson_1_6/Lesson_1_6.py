# import random

# def Random (start, end):
#     return random.randrange(start, end)

# global endRandomNumber
# global urinishlar

# while True:
#     endRandomNumber = int(input("""Siz bilan bir o'yin o'ynamoqchiman.
#     Men 1 dan nechagacha son o'ylay min(10) max(1000)"""))

#     urinishlarNumber = int(input("Siz nechta urinishga ega bo'lmoqchisiz min(3) max(10)"))

#     if endRandomNumber >=10 and endRandomNumber <=1000 and urinishlarNumber >=3  and urinishlarNumber <= 10:
#         break


# randomNumber = Random(1,endRandomNumber)

# for num in range(1,urinishlarNumber +1):

#     inputnumber =int(input(f"Siz son kiriting {endRandomNumber} /n >>>"))

#     if inputnumber < endRandomNumber:
#         print("Siz katta son kiriting >>>")
        
#     elif  inputnumber > endRandomNumber:
#        print("Siz kichik son kiriting >>>")

#     elif inputnumber == endRandomNumber:
#         print(f"Siz yutdingiz.Siz {num} ta urinishda topdingiz >>>") 
#         break

#     if urinishlarNumber -1 == num:
#         print(f"Siz yutqazdingiz.Men o'ylagan son shu {endRandomNumber} >>>")
#         break

# dostlar = []          # bo'sh ro'yxat
# print("5 ta eng yaqin do'stingiz kim?")
# for n in range(5):        # n bu yerda 0 dan 4 gacha qiymatlar oladi
#     dostlar.append(input(f"{n+1}-do'stingizning ismini kiriting: "))
# print(dostlar)

import random

def Random (start: int, end: int) -> int:
    return random.randrange(start, end)


while True:
    
    endRandomNumber = int(input("""Siz bilan Bir o'yin o'ynamoqchiman.
    Men nechagacha son o'ylay min(10) max(1.000)"""))

    urinishlarNumber = int(input("Siz nechta urinishga ega bo'lmoqchimiz min(3) max(10)"))

    if endRandomNumber >=10 and endRandomNumber <=1000 and urinishlarNumber >=3  and urinishlarNumber <= 10:
        break

randomNumber = Random(1, endRandomNumber)

for num in range(1, urinishlarNumber + 1):

    inputnumber = int(input(f"Siz son kiriting 1 dan {endRandomNumber} gacha >>> "))

    if inputnumber < randomNumber:
        print("Siz kichik son kiritdingiz. Katta son kiriting >>> ")
        
    elif  inputnumber > randomNumber:
       print("Siz katta son kiritingiz. Kichik son kiriting >>> ")

    elif inputnumber == randomNumber:
        print(f"Siz yutdingiz.Siz {num} ta urinishda topdingiz >>>") 
        break

    if urinishlarNumber -1 == num:
        print(f"Siz yutqazdingiz.Men o'ylagan son shu {randomNumber} >>>")
        break