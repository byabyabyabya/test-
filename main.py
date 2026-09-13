from calcul_mod.arifm import add, minus, delit, umnozit
from calcul_mod.advanced import power, square
def main():
    operation = input("введите операцию: (+, -, *, /, **, **2 ): ")
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
        a = int(input("введите gth число:"))
        b = int(input("введите второе число:"))
        res = umnozit(a, b)        
    elif (operation == "/"):
        a = int(input("введите первое число:"))
        b = int(input("введите второе число:"))
        res = delit(a,b)      
    elif (operation == "**"):
            a = int(input("введите первое число:"))
            b = int(input("введите второе число:"))
            res = power(a,b)     
    elif (operation == "**2"):
                a = int(input("введите число:"))
                res = square(a)      
    print("Результат:", res)  
if __name__ == "__main__":
    main()