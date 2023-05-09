# import random
# def harftop(start: str, end: str) -> str:
#     return random.randrange(start, end)

# while True:
#     print("===>>> Siz sontop bo'limiga xush kelibsiz <<<===")

#     endRandomAlfa = input("""
# Siz bilan bir o'yin o'ynamoqchiman.
# Men harf o'ylayman siz topasiz >>> 
# Men qaysi farfgach harf o'ylay min(i) max(ng) >>> : """)
    
#     urinishlarNumber = input("""
# Siz nechta urinishga ega bo'lmoqchisiz?
# min(5) max(15) >>> : """)
    
#     if endRandomAlfa == 'i' and endRandomAlfa == 'ng' and urinishlarNumber <= 5 and urinishlarNumber >15:
#         break

# RandomAlfa = harftop('a', endRandomAlfa)

# for num in range(1, urinishlarNumber +1):

#     inputalfa = int(input(f"Siz a dan {endRandomAlfa} gacha harf kiriting >>> : "))

#     if inputalfa < RandomAlfa:
#         print("Men o'ylagan harf bu emas.Boshqa harf kiritib ko'ring >>> : ")

#     elif inputalfa > RandomAlfa:
#         print("Men o'ylagan harf bu emas.Boshqa harf kiritib ko'ring >>> : ")

#     elif inputalfa == RandomAlfa:
#         print(f"Siz yutdingiz va {num} ta urinishda topdingiz >>>")

#     if inputalfa -1 == num:
#         print("Siz yutqazdingiz.Men o'ylagan harf bu emas >>>")
#         break

#  <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<!!!>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# import random

# def qoldigini_top(start: int, end: int) -> float:
#     return random.randrange(start, end)


# while True:

#     print("===>>> Siz QOLDIGINI_TOP bo'limiga xush kelibsiz <<<===")

#     endRandomNumber = float(input("""
# Siz bilan bir o'yin o'ynamoqchiman.
# Men son o'ylayman siz qoldig'ini topasiz.
# Men nechagacha son o'ylay? min(10.0) max(100.0) >>> : """))
    
#     urinishlarNumber = float(input("""
# Siz nechta urinishga ega bo'lmoqchisiz?
# min(5) max(10) >>> : """))
    
#     if endRandomNumber >= 10.0 and endRandomNumber <= 100.0 and urinishlarNumber >= 5 and urinishlarNumber <= 100 :
#         break

# RandomNumber = qoldigini_top(1.0, endRandomNumber)

# for num in range(1, int(urinishlarNumber) + 1):

#     inputnumber = float(input(f"Siz 1.0 dan {endRandomNumber} gacha bo'lgan sonlarning qoldig'ini kiriting >>> : "))

#     if inputnumber < RandomNumber:
#         print("Men o'ylagan sonning qoldig'i bu emas.Boshqa son kiriting : ")

#     elif inputnumber > RandomNumber:
#         print("Men o'ylagan sonning qoldig'i bu emas.Boshqa son kiriting : ")

#     elif inputnumber == RandomNumber:
#         print(f"Siz yudingiz va {num} ta urinishda topdingiz >>>")

#     if inputnumber -1.0 == num:
#         print(f"Siz yutqazdingiz.Men o'ylagan sonning qoldig'i shu {num}")
#         break

"""
    Login System

        userdan email va password olishingiz kerak bo'ladi.
        email qoidalari:

            @gmail.com oxirida yozilgan bo'lishi kerak. 
            boshida esa harfalar va sonlar ishtirok etish kerak.
            Harflar kichik bolishi kerak. Son va harflarning uzunligi 10 ta bo'lsin. 


        password qoidalari:

            min 3 ta kichik harf qatnashi kerak
            min 3 ta katta harf qatnashi kerak.
            min 3 ta son qatnashi kerak
            min 3 ta !---@---#---$---%---^---&---*---(---)---=---+ shular qatnashi kerak.
            minmum uzunligi 12 ta bo'lsin maxmum 20 ta bo'lsin.
"""


# def EMAIL__CHECK (email: str) -> bool:
#     boolean = False
    
#     if email[-10:] == "@gmail.com": 
#         if len(email[0:-10]) >= 10:
#             boolean = True
#         else: print("Sizni emailingizda kichik harflar va sonlar ishtirok etish kerak. \n Uzunligi 10 tadan katta bo'lishi kerak")
#     else: print("Siz emailingizda '@gmail.com' kiritmadingiz.")
    
#     return boolean

# def PASSWORD__CHECK (password: str) -> bool:
#     boolean = False

#     check__dict = {
#         "lower": 0,
#         "upper": 0,
#         "digit": 0,
#         "alpha": 0
#     }

#     for i in password:
#         if i.islower():
#             check__dict['lower'] += 1
#         elif i.upper(): 
#             check__dict['upper'] += 1
#         elif i.isdigit():
#             check__dict['digit'] += 1
#         elif i.isalpha():
#             check__dict['alpha'] += 1

#     if check__dict['lower'] >= 3 and check__dict['upper'] >= 3 and check__dict['digit'] >= 3 and check__dict['alpha'] and 12 <= len(password) <= 20:
#         boolean = True

#     return True

# def LOGIN():

#     while True:
#         print("<<<=== Siz LOGIN bo'limiga xush kelibsiz ===>>>")
#         email = input("Siz gmailingizni kiriting >>> : ")
#         password = input("Siz passwordingizni kiriting >>> : ")

#         email__check__boolean = EMAIL__CHECK(email)
#         password__check__boolean = PASSWORD__CHECK(password)

#         if email__check__boolean and password__check__boolean:
#             print("Sizning email va parolingiz tasdidlandi.")
#             break
# LOGIN()

def EMAIL__CHECK(email: str) -> bool:
    boolean = False

    if email[-10:] == "@gmail.com":
        if len(email[0: -10]) >= 10:
        
            boolean = True

        else:
            print("""
                Sizning gmailingiz harflar va sonlardan tashkil topgan bo;lishi kerak.
                Uzunligi 10 tadan katta bo'lishi kerak.
            """)

    else:
        print("Siz emailingizda '@gmail.com' kiritmadingiz.")

    return boolean

def PASWORD__CHECK (pasword: str) -> bool:
    boolean = False

    check__dict = {
        "lower": 0,
        "upper": 0,
        "digit": 0,
        "alpha": 0
    }

    for i in pasword:
        if i.islower():
            check__dict['lower'] += 1
        elif i.upper(): 
            check__dict['upper'] += 1
        elif i.isdigit():
            check__dict['digit'] += 1
        elif i.isalpha():
            check__dict['alpha'] += 1

    if check__dict['lower'] >= 3 and check__dict['upper'] >= 3 and check__dict['digit'] >= 3 and check__dict['alpha'] and 12 <= len(pasword) <= 20:
        boolean = True

    return True
    
def LOGIN():
    while True:
        print("--->>> LOGIN bo'limiga xush kelibsiz <<<---")
        email = input("Siz emailingizni kiriting: ")
        pasword = input("Siz paswordingizni kiriting: ")

        email__check__boolean = EMAIL__CHECK(email)
        pasword__check__boolean = PASWORD__CHECK(pasword)

        if email__check__boolean and pasword__check__boolean:
            print("Sizning emailingiz va paswordingiz tasdiqlandi.")
            break
LOGIN()

