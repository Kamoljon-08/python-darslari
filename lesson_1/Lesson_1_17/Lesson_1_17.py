"""


    exam 1 day


    inputdan ma' lumot olasiz. Shu olgan ma' lumotlarni

        kichik harflar soni nechta ekanligini
        katta haflar soni nechta ekanligini
        sonlar nechta ekanligini topish kerak
        toq sonlar nechta ekanligini topishi kerak va juft sonlarni ham
        ummuniy uzunligini topish kerak

"""

def KICHIK__HARF(lower):
    count = 0
    for x in lower:
        if x.islower():
            count += 1

    return count

def KATTA__HARF(upper):
    count = 0
    for x in upper:
        if x.isupper():
            count += 1

    return count

def SONLAR__SONI(digit):
    count = 0
    for x in digit:
        if x.isdigit():
            count += 1

    return count

def TOQ__SON(digit):
    count = 0
    for x in digit:
        if x.isdigit():
            if int(x) % 2 != 0:
                count += 1

    return count

def JUFT__SON(digit):
    count = 0
    for x in digit:
        if x.isdigit():
            if int(x) % 2 == 0:
                count += 1

    return count    

def MENU():

    input__words = input("Kichik harflar kiriting: ")
    lower = KICHIK__HARF(input__words)
    upper = KATTA__HARF(input__words)
    all__digit = SONLAR__SONI(input__words)
    odd__digit = TOQ__SON(input__words)
    even__digit = JUFT__SON(input__words)

    print(f"Kichik haflar soni {lower} \n Katta haflar soni {upper} \n Sonlar soni {all__digit} \n Toq sonlar soni {odd__digit} \n Juft sonlar soni {even__digit}")

def MAIN():
    MENU()
MAIN()