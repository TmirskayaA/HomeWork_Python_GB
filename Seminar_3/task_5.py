#Задайте число. 
#Составьте список чисел Фибоначчи, 
#в том числе для отрицательных индексов.

#Пример:

#для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 

def Fibonacci(digit):
    if digit in [1, 2]: return 1
    else: return Fibonacci(digit-1) + Fibonacci(digit-2)

def NegaFibonacci(digit):
    if digit == 1: return 1
    elif digit == 2: return -1
    else:
        NumberOne, NumberTwo = 1, -1
        for i in range(2, digit):
            NumberOne, NumberTwo = NumberTwo, NumberOne - NumberTwo
        return NumberTwo

print('Здравствуте!')
number = int(input('Задайте число: '))

newArray = []

for i in range(1, number + 1):
    newArray.append(Fibonacci(i))
    newArray.insert(0, NegaFibonacci(i))

print(f'Получили следующий список: {newArray}')