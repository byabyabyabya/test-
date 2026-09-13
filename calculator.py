operation = input("введите операцию: (+, -, *, /): ")
a = 0
b = 0
if (operation == "+"):
    a = int(input("введите первое число:"))
    b = int(input("введите второе число:"))
    print(a+b)
elif (operation == "-"):
    a = int(input("введите уменьшаемое:"))
    b = int(input("введите вычитаемое:"))
    print(a-b)
elif (operation == "*"):
    a = int(input("введите первое число:"))
    b = int(input("введите второе число:"))
    print(a*b)
elif (operation == "/"):
    a = int(input("введите делимое:"))
    b = int(input("введите делитель:"))
    print(a/b)
fruits = [ "яблоко", "банан", "апельсин"]
x = 1
for x in range(3):
    print(fruits[x])
    x = x+1