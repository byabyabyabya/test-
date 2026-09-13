from calcul_mod.arifm import add, minus, delit, umnozit
def main():
    operation = input("введите операцию: (+, -, *, /): ")
    a = 0
    b = 0
    res = 0
    if (operation == "+"):
        a = int(input("введите первое число:"))
        b = int(input("введите второе число:"))
        res = add(a, b)
    elif (operation == "-"):
        a = int(input("введите первое число:"))
        b = int(input("введите второе число:"))
        res = minus(a, b)
    elif (operation == "*"):
        a = int(input("введите первое число:"))
        b = int(input("введите второе число:"))
        res = umnozit(a, b)        
    elif (operation == "/"):
        a = int(input("введите первое число:"))
        b = int(input("введите второе число:"))
        res = delit(a,b)      
    print("Результат:", res)  
if __name__ == "__main__":
    main()