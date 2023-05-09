BOOK = []

BOOK_1 = {
    "id": 1,
    "title": "Sariq dev",
    "anthor": "Axmatov Kamoljon",
    "number": 1234567891357903,
    "password": 7777,
    "price": 20.56,
    "balance": 10000,
    "page": 300,
    "dascription": "Sariq dev kitobi python haqida"
}

BOOK_2 = {
    "id": 2,
    "title": "Java_245",
    "anthor": "Sharopov Durbek",
    "number": 1234567891234567,
    "password": 7676,
    "price": 23.90,
    "balance": 6700,
    "page": 100,
    "dascription": "Sariq dev kitobi javascript haqida"
}

BOOK_3 = {
    "id": 3,
    "title": "Html_5432",
    "anthor": "Sharopov Bexro'z",
    "number": 9876543217654321,
    "password": 6767,
    "price": 10.40,
    "balance": 9100,
    "page": 150,
    "dascription": "Sariq dev kitobi html haqida"
}

BOOK_4 = {
    "id": 4,
    "title": "Css_df43",
    "anthor": "Normurodov Dilshod",
    "number": 3216549875437612,
    "password": 5757,
    "price": 54.56,
    "balance": 10045,
    "page": 170,
    "dascription": "Sariq dev kitobi css haqida"
}

BOOK_5 = {
    "id": 5,
    "title": "C++_5w3f",
    "anthor": "Ismoilov Bexro'z",
    "number": 5432112345698765,
    "password": 7575,
    "price": 25.67,
    "balance": 15056,
    "page": 250,
    "dascription": "Sariq dev kitobi c++ haqida"
}

BOOK.append(BOOK_1)
BOOK.append(BOOK_2)
BOOK.append(BOOK_3)
BOOK.append(BOOK_4)
BOOK.append(BOOK_5)

def LOGIN ():
    while True:
        print("=====>>> Siz LOGIN bo'limiga xush kelibsiz <<<=====")
        number_global = int(input("Siz raqamingizni kiriting: "))
        password_global = int(input("Siz parolingizni kiriting: "))

        if len(str(number_global)) == 16 and len(str(password_global)) == 4:
            break
        else:
            print("Siz kiritgan karta raqam yoki parol xato")

    for a in BOOK:

        if a['number'] == number_global and a['password'] == password_global:
            MENU()
        else:
            continue

def console__print(book__data):
    print(f"=======================================")
    print(f"===> ID: {book__data['id'] }")
    print(f"===> Title: {book__data['title']}")
    print(f"===> Another: {book__data['another']}")
    print(f"===> Number: {book__data['number']}")
    print(f"===> Password: {book__data['password']}")
    print(f"===> Price: {book__data['price']}")
    print(f"===> Balance: {book__data['balance']}")
    print(f"===> Page: {book__data['page']}")
    print(f"===> Description: {book__data['description']}")
    print(f"=======================================\n")

def PURCHASE():
    print("=====>>> Siz PURCHASE bo'limiga xush kelibsiz <<<=====")
    for i in BOOK:
        console__print(i)

def ANOTHER():
    print("=====>>> Siz ANOTHER bo'limiga xush kelibsiz <<<=====")
    pass

def PAGE():
    print("=====>>> Siz PAGE bo'limiga xush kelibsiz <<<=====")
    pass

def DESCRIPTION():
    print("=====>>> Siz DESCRIPTION bo'limiga xush kelibsiz <<<=====")
    pass

def PRICE():
    print("=====>>> Siz PRICE bo'limiga xush kelibsiz <<<<=====")
    pass

def BALANCE():
    print("=====>>> Siz BALANCE bo'limiga xush kelibsiz <<<=====")
    pass

def MENU():
    print("=====>>> Siz MENU bo'limiga xush kelibsiz <<<=====")
    print("""
    *****************************
    *****   1) Purchase     *****
    *****   2) Another      *****
    *****   3) Page         *****
    *****   4) Decription   *****
    *****   5) Price        *****
    *****   6) Balnce       *****
    *****   7) Exit         *****
    *****************************
    """)
    input__menu__number = int(input("Menudan birini tanlang: "))
    if input__menu__number == 1: PURCHASE()
    elif input__menu__number == 2: ANOTHER()
    elif input__menu__number == 3: PAGE()
    elif input__menu__number == 4: DECRIPTION()
    elif input__menu__number == 5: PRICE()
    elif input__menu__number == 6: BALANCE()
    elif input__menu__number == 7: EXIT()
    else: print("Menudagi sonlardan birini tanlang: ")

def MAIN():
    LOGIN()

MAIN()
