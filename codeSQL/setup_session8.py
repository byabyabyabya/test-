import psycopg2
DB_NAME = 'sells_data'
DB_USER = "postgres"
DB_PASSWORD = 'postgres'

purchases = [
    ("sok",10, 23, "2026-10-10"), 
    ("chay", 20, 50, "2026-10-11"),
    ("voda", 30, 20, "2026-10-10"),
    ("chay", 200, 50, "2026-10-12"),
    ("sok",5, 23, "2026-10-13"), 
]

with psycopg2.connect(
    dbname = DB_NAME, user = DB_USER, password = DB_PASSWORD, host = "127.0.0.1", port =5432
) as connection:
    with connection.cursor() as cursor:
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS lesson8_receipts (
        id SERIAL PRIMARY KEY, 
        product_name TEXT NOT NULL,
        quantity INTEGER NOT NULL,
        price NUMERIC (10, 2) NOT NULL, 
        sale_date DATE NOT NULL
        )
        """)
        cursor.execute("DELETE FROM lesson8_receipts")
        for purchase in purchases:
            cursor.execute("""
            INSERT INTO lesson8_receipts
                (product_name, quantity, price, sale_date)
            VALUES (%s, %s, %s, %s )

            """, purchase)
connection.close()
print("гтово")
