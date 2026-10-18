import matplotlib.pyplot as plt
import psycopg2
connection = psycopg2.connect(
    dbname = 'postgres', 
    user = "postgres", 
    password = "postgres", 
    host = "127.0.0.1",
    port = "5432"
)
cursor = connection.cursor()


cursor.execute("""
SELECT product_name, SUM(quantity * price) AS total_revenue
FROM sells
GROUP BY product_name
ORDER BY total_revenue DESC
""")

revenue_data = cursor.fetchall()

cursor.close()
connection.close()

dates = [row[0] for row in revenue_data]
quantity = [row[1] for row in revenue_data]

plt.figure(figsize=(10, 6))
plt.plot(dates, quantity, marker="o", color = "#DD37B4")
plt.title("Кол. проданных товаров по дням")
plt.xlabel("Дата")
plt.xlabel("Проданные товары")
plt.xticks(rotation = 45)
plt.show()