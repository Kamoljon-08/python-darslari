# b = "MiRaFzal"
# # b = ""
# for num in b:
#     if num.isupper():
#        b += num.lower()
#     else:
#         b += num.upper()
# print(b)
        
# print("meniki", b.swapcase())

# a = input("Soz kiriting: ")
# for x in range(1, 20):
#     if len(a) < 15:
#         a += "-"
# print(a)
  

# b = ("Tentakning tajribasi", "Boburnoma", "Sadiy Iskandariy", "Hayrat-ul Abror")
# if "Boburnoma" in b:
#     print("Ha, Boburnoma bor")
# else:
#     print("Boburnoma yo'q")
    

# a = ("kitob", "daftar", "ruchka")
# if "kitob" in a:
#     print(" Ha, kitob bor")
# else:
#     print("Kitob yo'q")


# '''
#     a dan b gacha bo'lgan barcha 
#     butun sonlar yig'indisini 
#     chaqiruvchi programma
# '''
# a = int(input("Sonni kiriting A: "))
# b = int(input("Sonni kiriting B: "))
# if a < b:
#     for num in range(a, b +1):
#         print(b - num)


# '''
# a va b butun sonlar berilgan (a < b). 
# a va b sonlari orasidagi barcha butun sonlarni (a va b dan tashqari)
# kamayish tartibida chaqiruvchi va chaqirilgan sonlar sonini 
# chaqiruvchi programma 
# '''
# a = int(input("Sonni kiriting A: "))
# b = int(input("Sonni kiriting B: "))
# allnum = 1
# for bir in range(a, b +1):
#     allnum *= bir
# print(allnum)

# '''
# a dan b gacha bo'lgan barcha butun sonlarni 
# darajaga oshirib chaqiruvchi programma
# '''
# a = int(input("Sonni kiriting A: "))
# b = int(input("Sonni kiriting B: "))
# for _num_ in range(a, b +1):
#     print(_num_**2)

# a = int(input("Sonni kiriting A: "))
# b = int(input("Sonni kiriting B: "))
# for son in range(a,b +1):
#     print(son **4)

# '''
#     a dan b gacha bo'lgan barcha 
#     butun sonlar ko'paytmasini 
#     chaqiruvchi programma
# '''
# a = int(input("Sonni kiriting"))
# sum = a * (a - 2) * (a - 4)
# print(sum)
# if sum % 2 == 0:
#     print(2)
# else: 
#     print(1)


# a = int(input("Sonni kiriting"))
# num = a * (a - 4) * (a - 6)
# print(num)
# if num % 2 == 0:
#     print(2)
# else:
#     print(1)

# a = ('1','2','3','4')
# b = tuple()
# print(a)
# print(max(a))
# print(min(a))
# print(a.count("2"))
# print(a.index("1"))
# print(any(a))
# print(any(b))
# print(len(a))