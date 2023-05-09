# from uuid import uuid4
# BOOK_1 = {
#     "id": uuid4(),
#     "title": "Sariq dev",
#     "anthor": "Axmatov Kamoljon",
#     "number": 1234567891357903,
#     "password": 7777,
#     "price": 20.56,
#     "balance": 10000,
#     "page": 300,
#     "dascription": "Sariq dev kitobi python haqida"
# }
# a = "d0e899e6-8c72-4f05-8f3f-edddc64c9fba"
# b = "f0315bc1-bb3e-4061-bbc1-4051d39d4438"

# a = uuid4()

# print(type (a))




# import datetime as dt

# x = dt.datetime.now()

# print(x.strftime("%y__%m__%X"))
# print(x.strftime("%B/%d"))
# print(x.strftime("%X:%d"))
# print(x.strftime("%m-%y"))
# print(x.strftime("%b--%W--%j--%B"))

"""
    peshingi 12:00 -> 23:59 PM
    ertalabki 00:00 -> 11:59 AM

"""

"""
    yil__oy__kun__toliq vaqt

    oy/kun

    vaqt:kun


    oy-yil

    Oy nomi qisqa--Nechta hafra kuni--Shu kungacha necha kunligi--OY nomi kengaytmasi
"""

# print(platform.system())

"""
    def l ():
        pass

    def k ():
        pass

    main.py

    login.py

    register.py


"""



from platform import platform
from uuid import uuid4
from datetime import datetime
from platform import system

PRODUCTS = []
laptop__buy__id = []

products_1 = {
    "id": uuid4(),
    "title": "Kamoljon",
    "brand": "ACER",
    "price": 1345.89,
    "stars": 5,
    "model": "ACER xl 10",
    "image": "images.jpeg",
    "discount": 30,
    "category": "New",
    "create__data": datetime.now(),
    "platform": platform(),
    "color": ["white, red, black"],
    "description": "id: 1, title: Kamoljon, brand: ACER, price: 1345.89, stars: 5, model: ACER xl 10, image: images.jpeg, discount: 30, category: New, create__data: 1, platform: Windows, color: [white, red, black]"
}

products_2 = {
    "id": uuid4(),
    "title": "Mirafzal",
    "brand": "MSI",
    "price": 1350.99,
    "stars": 4,
    "model": "MSI xl 9",
    "image": "noutbook.jpeg",
    "discount": 40,
    "category": "New",
    "create__data": datetime.now(),
    "platform": platform(),
    "color": ["black, blue, red"],
    "description": "id: 2, title: Mirafzal, brand: MSI, price: 1350.99, stars: 4, model: MSI xl 9, image: noutbook.jpeg, discount: 40, category: New, create__data: 2, platform: MacOs, color: [black, blue, red]"
}

products_3 = {
    "id": uuid4(),
    "title": "Durbek",
    "brand": "HP",
    "price": 1355.87,
    "stars": 4,
    "model": "Hp xl 8",
    "image": "komputer.jpeg",
    "discount": 50,
    "category": "New",
    "create__data": datetime.now(),
    "platform": platform(),
    "color": ["red, green, black"],
    "description": "id: 3, title: Durbek, brand: HP, price: 1355.87, stars: 4, model: Hp xl 8, image: Komputer.jpeg, discount: 50, category: New, create__data: 3, platform: Debian, color: [red, green, black]"
}

PRODUCTS.append(products_1)
PRODUCTS.append(products_2)
PRODUCTS.append(products_3)

def CONSOLE__PRINT(products__data):
    print(f"=======================================")
    print(f"===> id: {products__data['id'] }")
    print(f"===> title: {products__data['title']}")
    print(f"===> brand: {products__data['brand']}")
    print(f"===> price: {products__data['price']}")
    print(f"===> stars: {products__data['stars']}")
    print(f"===> model: {products__data['model']}")
    print(f"===> image: {products__data['image']}")
    print(f"===> discount: {products__data['discount']}")
    print(f"===> category: {products__data['category']}")
    print(f"===> create__data: {products__data['create__data']}")
    print(f"===> platform: {products__data['platform']}")
    print(f"===> color: {products__data['color']}")
    print(f"===> description: {products__data['description']}")
    print(f"=======================================\n")

def SEE__ALL():
    print("===>>> SEE ALL bo'limiga xush kelibsiz <<<===")
    for x in PRODUCTS:
        CONSOLE__PRINT(x)
    MENU()

def BUYING__LAPTOP(input__products):

    check__boolean = {
        "id": "",
        "title": "",
        "brand": "",             
        "price": 0,
        "stars": 0,
        "model": "",
        "image": "",
        "discount": 0,
        "category": "",
        "create__data": 0,
        "platform": "",
        "color": [],
        "description": ""
    }
        
    # id = last__laptop['id'] + 1
    check__boolean['id'] = uuid4()
    check__boolean['platform'] = platform()
    check__boolean['create__data'] = datetime.now()
    check__boolean['title'] = input("Siz titleyingizni kiriting: ")
    check__boolean['brand'] = input("Siz brandingizni kiriting: ")
    check__boolean['price'] = float(input("Siz pricengizni kiriting: "))
    check__boolean['stars'] = int(input("Siz starsingizni kiriting: "))
    check__boolean['model'] = input("Siz modelingizni kiriting: ")
    check__boolean['image'] = input("Siz imagengizni kiriting: ")
    check__boolean['discount'] = int(input("Siz discountingizni kiriting: "))
    check__boolean['category'] = input("Siz categoryingizni kiriting: ")
    check__boolean['color'] = input("Siz coloringizni kiriting: ")
    check__boolean['description'] = input("Siz descriptioningizni kiriting: ")

    PRODUCTS.append(check__boolean)
    MENU()

def PRODUCTS__CREATE():
    print("===>>> PRODUCTS CREATE bo'limiga xush kelibsiz <<<===")

    for i in PRODUCTS:
        BUYING__LAPTOP(i)
    MENU()

def MENU():
    print("===>>> MENU bo'limiga xush kelibsiz <<<===")
    print("""
    ===============================
    =====   See all           =====
    =====   Product create    =====
    ===============================
    """)
    input__menu__number = int(input("Menudan birini tanlang: "))
    if input__menu__number == 1: SEE__ALL()
    elif input__menu__number == 2: PRODUCTS__CREATE()
    else: print("Menudagi sonlardan birini tanlang: ")

def MAIN():
    MENU()

MAIN()