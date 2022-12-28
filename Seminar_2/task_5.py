#Реализуйте алгоритм перемешивания списка.

print('Здравствуте!')
number = int(input('Сколько чисел хотите видеть в списке? '))

import random
numberMass = []

for i in range(0, number):
    numberMass.insert(i, int(random.randrange(0,9)))

print(f"Получили массив: {numberMass}")

random.shuffle(numberMass)

print(f"Перемешали список: {numberMass}")