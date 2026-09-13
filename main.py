from calcul_mod.arifm import add, minus, delit, umnozit
from calcul_mod.advanced import power, square, root

class NegativeError(Exception):
     pass

def sqrt_check(a):
     if (a<0):
          raise NegativeError("оштбка. корень из отрицательного числа не извлечен")
     return root(a)

def main():
    try:
        operation = input("введите операцию: (+, -, *, /, **, **2 , **0.5): ")
        a = 0
        b = 0
        res = 0
        if (operation == "+"):
            a = int(input("введите первое число:"))
            b = int(input("введите второе число:"))
            res = add(a, b)
            print("Результат:", res)  
        elif (operation == "-"):
            a = int(input("введите первое число:"))
            b = int(input("введите второе число:"))
            res = minus(a, b)
            print("Результат:", res)  
        elif (operation == "*"):
            a = int(input("введите gth число:"))
            b = int(input("введите второе число:"))
            res = umnozit(a, b)   
            print("Результат:", res)       
        elif (operation == "/"):
            a = int(input("введите первое число:"))
            b = int(input("введите второе число:"))
            res = delit(a,b)   
            print("Результат:", res)     
        elif (operation == "**"):
                a = int(input("введите первое число:"))
                b = int(input("введите второе число:"))
                res = power(a,b)    
                print("Результат:", res)   
        elif (operation == "**2"):
                    a = int(input("введите число:"))
                    res = square(a) 
                    print("Результат:", res)    
        elif (operation == "**0.5"):
                    a = int(input("введите число:"))
                    res = sqrt_check(a)
                    print("Результат:", res)   
        else:
             print("произошла ошибка. возможно, стоит перестать писать околесицу")  
    
    except ZeroDivisionError:
        print("на ноль делить нельзя")
    except ValueError:
        print("это не число.")
    finally:
        print("всё")

if __name__ == "__main__":
    main()