#Задайте список из вещественных чисел. 
#Напишите программу, которая найдёт разницу 
#между максимальным и минимальным значением дробной части элементов.

#Пример:

# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

def FillRandomArray(quantity, minimum, maximum):
    import random
    array = []
    for i in range(0, quantity):
        array.insert(i, round(float(random.uniform(minimum,maximum)), 2))
    return array

def DifferenceMixMaxFractional(array):
    fractionalArray = []
    for i in range(0, len(array)):
        fractionalArray.append(int((array[i]*100)%100))
    
    min = 100
    max = 0
    for i in range(0, len(fractionalArray)):
        if fractionalArray[i] < min: min = fractionalArray[i]
        elif fractionalArray[i] > max: max = fractionalArray[i]
    
    difference = (max - min)/100
    return difference

print('Здравствуте!')
number = int(input('Сколько чисел хотите видеть в списке? '))

newArray = FillRandomArray(number, 1, 9)

print(f"Получили массив: {newArray}")

print(f'Разница между максимальным и минимальным значением = {DifferenceMixMaxFractional(newArray)}')


