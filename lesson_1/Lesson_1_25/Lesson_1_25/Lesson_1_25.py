import os 

number = input("Katta harf, kichik harf va sonlardan tashkil topgan matn kiriting: ")

for i in number:
    if i.isupper():
        if not os.path.exists("Lesson_1_25/katta_harflar.txt"):
            b = open("Lesson_1_25/katta_harflar.txt", "x")

        f = open("Lesson_1_25/katta_harflar.txt", "a")
        f.write(f"{i} ")
        f.close()

    if i.islower():
        if not os.path.exists("Lesson_1_25/kichik_harflar.txt"):
            s = open("Lesson_1_25/kichik_harflar.txt", "x")

        c = open("Lesson_1_25/kichik_harflar.txt", "a")
        c.write(f"{i} ")
        c.close()

    if i.isdigit():
        if not os.path.exists("Lesson_1_25/sonlar.txt"):
            x = open("Lesson_1_25/sonlar.txt", "x")

        z = open("Lesson_1_25/sonlar.txt", "a")
        z.write(f"{i} ")
        z.close()