with open ("note.txt", "a", encoding="utf-8") as file:
    file.write("1. это лдфовылдыфо \n ")

with open ("note.txt", "a", encoding="utf-8") as file:
    file.write(" 2. это фыавфыв \n ")

note = input("введите текст")
with open ('note.txt', "a", encoding="utf-8") as file:
    file.write(note + "\n")

with open ('note.txt', "r", encoding="utf-8") as file:
    print(file.read())