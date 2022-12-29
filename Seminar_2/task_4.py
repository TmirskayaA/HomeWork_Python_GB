#Задайте список из N элементов, 
#заполненных числами из промежутка [-N, N]. 
#Найдите произведение элементов на указанных позициях. 
#Позиции хранятся в файле file.txt в одной строке одно число.

print('Здравствуте!')
number = int(input('Напишите число: '))

import random

file = open('file(4inS2).txt', 'a')
for i in range(1, number+1):
    a = int(random.randrange(-number, number))
    file.write(f'{a}')
file.close()

#Найдите произведение элементов на указанных позициях. // Т.к. нет примера, я ни разу не поняла, что вы хотите увидеть. 
# Ваше объяснение в семинаре мне тоже не особо помогло, так что как поняла, так поняла.

file = open('file(4inS2).txt', 'r')
string = file.readline()
file.close()

numberMass = []
a = 0

for i in range(0, len(string)):
    if string[i] == '-':
        a = int(string[i]+string[i+1])
        numberMass.append(a)
    elif i == 0:
        a = int(string[i])
        numberMass.append(a)
    elif int(string[i])*-1 not in numberMass: 
        a = int(string[i])
        numberMass.append(a)

product = 1

for i in range(0, len(numberMass)):
    product *= numberMass[i]

print(f'Произведение чисел массива: {numberMass} = {product}.')

answer = str(input('Отчищаем файл? Напишите \"Да\" или \"Нет\": '))
while answer != 'Да' and answer != 'Нет':
    answer = str(input('Вы написали что-то не то. Напишите \"Да\" или \"Нет\": '))
if answer == 'Да': 
    file = open('file(4inS2).txt', 'w')
    file.close()
else: exit()




