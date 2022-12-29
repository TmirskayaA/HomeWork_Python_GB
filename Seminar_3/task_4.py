#Напишите программу, 
#которая будет преобразовывать 
#десятичное число в двоичное.

#Пример:

# 45 -> 101101
# 3 -> 11
# 2 -> 10

def ToBinary(digit):
    max = digit
    while digit != 0:
        if digit == max: binary = str(digit % 2)
        else: binary = str(digit % 2) + binary
        digit //= 2
    return binary

print('Здравствуте!')
number = int(input('Какое число хотите преобрпазовать в двоичное? '))

if number == 0: 
    print('0 в двоичной системе останется нулём.')
    exit()
elif number < 0:
    print('Такое я пока не умею.')
    exit()

print(f'Число {number} в двочной сисеме = {ToBinary(number)}')