import csv 
filename ="books.csv"
with open("books.csv","w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Название", "Автор" ])
    writer.writerow(["Скотный двор", "Джордж Оруелл" ])
    writer.writerow(["Сердца трех", "Джек Лондон" ])
    writer.writerow(["Мастер и Маргарита", "Михаил Афанасиевич Булгаков" ])
    writer.writerow(["451 градус по Фаренгейту", "Рей Бредберри" ])

with open(filename, "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
with open(filename, "r", encoding="utf-8") as file:
     reader = csv.reader(file)
     for title, author in reader:
        print(f"{title} - {author}")