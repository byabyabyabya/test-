from calcul_mod.arifm import add, minus, delit, umnozit
from calcul_mod.advanced import power, square, root
from calcul_mod.triganometry import siiin, cosinus, tangens, cotangens
import sys
sys.stdout.reconfigure(encoding='utf-8')
sys.stdin.reconfigure(encoding='utf-8')

class NegativeError(Exception):
     pass

def sqrt_check(a):
     if (a<0):
          raise NegativeError("\n \033[43;30m ошибка. Корень из отрицательного числа не извлечен\033[0m")
     return root(a)

def main():
    try:
        isEnd = False
        while (isEnd == False):
            operation = input("введите операцию \n \n (+, -, *, /, **, **2 , **0.5, $#,(0, !#, (0!# ),  \n \n или напишите (справка) или для получения доп. инф.")
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

            #тригономметрия 
            elif (operation == "$#" or operation == "синус"):
                a = int(input("введите число:"))
                res = siiin(a)
                print("Результат:", res, "  Приблизительно равно:", round(res, 3))   
                isEnd = True
            elif (operation == "(0" or operation == "косинус"):
                a = int(input("введите число:"))
                res = cosinus(a)
                print("Результат:", res, "  Приблизительно равно:", round(res, 3))   
                isEnd = True
            elif (operation == "!#" or operation == "тангенс"):
                a = int(input("введите число:"))
                if a % 180 == 90:
                    print("ошибка. из этого числа нельзя вычислить тангенс")
                else:
                    res = tangens(a)
                    print("Результат:", res, "  Приблизительно равно:", round(res, 3))   
                isEnd = True
            elif (operation == "(0!#" or operation == "котангенс"):
                a = int(input("введите число:"))
                if a % 180 == 0:
                    print("ошибка. из этого числа нельзя вычислить котангенс")
                else:
                    res = tangens(a)
                    print("Результат:", res, "  Приблизительно равно:", round(res, 3))   
                isEnd = True


            elif (operation == "справка"):
                print("\n Команды в этом калькуляторе написаны таким образом, чтобы их удобно было вводить и на русской раскладке, и на английской, но также вы всегда можете написать команду другим способом")
                print("Ниже будет представлен список всех доступных команд, а также их эквивалент на русском языке.")
                print("\n\n Арифметика: \n \"+\" -- \"сложение;\"\n \"-\" -- \"вычитание;\"\n \"*\" -- \"умножение;\"\n \"/\" -- \"деление;\"\n \"**\" -- \"степень;\"\n \"**2\" -- \"квадрат;\"\n \"**0.5\" -- \"корень\"(квадратный)\n")
                print("\n Тригонометрия: \n \"$#\" -- \"синус\"\n \"(0\" -- \"косинус\"\n \"!#\" -- \"тангенс\"\n \"(0!#\" -- \"котангенс\"")
            else:
                print("\033[43;30m произошла ошибка. либо это опечатка, либо вы написали это сознательно. в таком случае,прекращайте баловаться!\033[0m")  
    
    except ZeroDivisionError:
        print("\n \033[43;30m на ноль делить нельзя\033[0m")
    except KeyboardInterrupt:
        print("\n \033[43;30m Программа остановлена.\033[0m")
    except ValueError:
        print("\n \033[43;30m это не число.\033[0m")
    finally:
        print("всё")

if __name__ == "__main__":
    main()