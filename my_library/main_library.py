import csv
FILENAME = "my_books.csv"

def add_book(title, author):
    with open(FILENAME, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([title, author ])
def show_books():
    try:
        with open(FILENAME, "r", encoding="utf-8"):
            reader = csv.reader(file)
            books = list(reader)
    except FileNotFoundError:
        print("Файл не найденю пока что нет книг")        
        return
    if not books:
        print("книг пока что нет")
        return
    print("Ваши книги:")
    for i, book in enumerate(books, 1):
        title, author = book
        print(f"{i}. {title} -- {author}")
#def main():
