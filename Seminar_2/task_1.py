#Напишите программу, 
#которая принимает на вход 
#вещественное число 
#и показывает сумму его цифр.

#Пример:

#- 6782 -> 23
#- 0,56 -> 11

print('Здравствуте!')
number = str(input('Напишите число: '))

sum = 0

for i in range(0, len(number)):
    if number[i].isdigit(): sum += int(number[i])

if sum == 0: print('Вы не написали число!')
else: print(f'Сумма цифр = {sum}')