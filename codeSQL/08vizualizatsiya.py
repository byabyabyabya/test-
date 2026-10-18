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

products = [row[0] for row in revenue_data]
revenue = [row[1] for row in revenue_data]

plt.figure(figsize=(10, 6))
plt.bar(products, revenue, color = "#DD37B4", alpha = 0.7)
plt.title("Общ. выручка по продуктам")
plt.xlabel("Продукт")
plt.xlabel("Выручка")
plt.show()