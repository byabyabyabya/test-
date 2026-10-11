import psycopg2
connection = psycopg2.connect(
    dbname = 'postgres', 
    user = "postgres", 
    password = "postgres", 
    host = "127.0.0.1",
    port = "5432"
)

connection.autocommit = True
cursor = connection.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS sells (
    id SERIAL PRIMARY KEY, 
    product_name VARCHAR(100),
    quantity INT ,
    price DECIMAL ,
    sell_date DATE
)
""")
print("Таблица создана")

cursor.close()
connection.close()