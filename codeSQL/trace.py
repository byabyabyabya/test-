sales_data = [
    ("Tea", 10, 100), 
    ("Bread", 30, 20), 
]
for sale in sales_data:
    name = sale[0]
    money = sale[1] * sale[2]
    print(name, money)
print("готово")