from calcul_mod.arifm import add, minus, delit, umnozit
from calcul_mod.advanced import power, square, root
from calcul_mod.triganometry import siiin
import sys
sys.stdout.reconfigure(encoding='utf-8')
sys.stdin.reconfigure(encoding='utf-8')

class NegativeError(Exception):
     pass

def sqrt_check(a):
     if (a<0):
          raise NegativeError("оштбка. Корень из отрицательного числа не извлечен")
     return root(a)

def main():
    try:
        isEnd = False
        while (isEnd == False):
            operation = input("введите операцию (+, -, *, /, **, **2 , **0.5, $#, ), или напишите (справка) или для получения доп. информации ")
            a = 0
            b = 0
            res = 0
            if (operation == "+" or operation == "сложение"):
                a = int(input("введите первое число:"))
                b = int(input("введите второе число:"))
                res = add(a, b)
                print("Результат:", res)  
                isEnd = True
            elif (operation == "-" or operation == "вычитание"):
                a = int(input("введите первое число:"))
                b = int(input("введите второе число:"))
                res = minus(a, b)
                print("Результат:", res)  
                isEnd = True
            elif (operation == "*" or operation == "умножение"):
                a = int(input("введите первое число:"))
                b = int(input("введите второе число:"))
                res = umnozit(a, b)   
                print("Результат:", res) 
                isEnd = True      
            elif (operation == "/" or operation == "деление"):
                a = int(input("введите первое число:"))
                b = int(input("введите второе число:"))
                res = delit(a,b) 
                isEnd = True  
                print("Результат:", res)     
            elif (operation == "**" or operation == "степень"):
                    a = int(input("введите первое число:"))
                    b = int(input("введите второе число:"))
                    res = power(a,b)    
                    print("Результат:", res) 
                    isEnd = True  
            elif (operation == "**2" or operation == "квадрат"):
                    a = int(input("введите число:"))
                    res = square(a) 
                    print("Результат:", res)  
                    isEnd = True  
            elif (operation == "**0.5" or operation == "корень"):
                        a = int(input("введите число:"))
                        res = sqrt_check(a)
                        print("Результат:", res) 
                        isEnd = True  
            elif (operation == "$#" or operation == "синус"):
                        a = int(input("введите число:"))
                        res = siiin(a)
                        print("Результат:", res, "  Приблизительно равно:", round(res, 3))   
                        isEnd = True
            elif (operation == "справка"):
                print("\n Команды в этом калькуляторе написаны таким образом, чтобы их удобно было вводить и на русской раскладке, и на английской, но также вы всегда можете написать команду другим способом")
                print("Ниже будет представлен список всех доступных команд, а также их эквивалент на русском языке.")
                print("\n\n Арифметика: \n \"+\" -- \"сложение;\"\n \"-\" -- \"вычитание;\"\n \"*\" -- \"умножение;\"\n \"/\" -- \"деление;\"\n \"**\" -- \"степень;\"\n \"**2\" -- \"квадрат;\"\n \"**0.5\" -- \"корень\"(квадратный)\n")
                print("\n Тригонометрия: \n \"$#\" -- \"синус\"")
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