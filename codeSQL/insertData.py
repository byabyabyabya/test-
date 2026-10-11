import psycopg2
from datetime import datetime
connection = psycopg2.connect(
    dbname = 'postgres', 
    user = "postgres", 
    password = "postgres", 
    host = "127.0.0.1",
    port = "5432"
)

connection.autocommit = True
cursor = connection.cursor()

cursor.execute("DELETE FROM sells")
sells_data = [
    ("молоко", 10, 700, datetime(2026, 1, 10) ), 
    ("белый хлеб", 25, 300, datetime(2026, 2, 24)), 
    ("черный хлеб", 34, 500, datetime(2026, 3, 10)),
    ("Черный чай", 23, 300, datetime(2026, 3, 5)), 
    ("ЗЕЛЕНЫЙ ЧАЙ", 15, 200, datetime(2026, 4, 5 ))
]
for sell in sells_data:
    cursor.execute("INSERT INTO sells (product_name, quantity, price, sell_date) VALUES (%s, %s, %s, %s)", sell)
connection.commit()
print("Данные добавлены")

cursor.close()
connection.close()