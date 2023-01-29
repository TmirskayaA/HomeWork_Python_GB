#Напишите программу, 
#которая на вход принимает два числа A и B, 
#и возводит число А в целую степень B с помощью рекурсии.

#A = 3; B = 5 -> 243 (3⁵)
#A = 2; B = 3 -> 8

def Exponentiation(digit, degree):
    if (degree == 1): return (digit)
    else: return (digit * Exponentiation(digit, degree - 1))

print('\nЗдравствуйте!\n')
number = int(input("Введите число: "))
degreeNumber = int(input("В какую степень возводим? "))

print(f'\nРезультат: {Exponentiation(number, degreeNumber)}')