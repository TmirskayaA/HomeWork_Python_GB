#Задайте последовательность чисел. 
#Напишите программу, 
#которая выведет список неповторяющихся элементов 
#исходной последовательности.

def FillRandomArray(quantity, minimum, maximum):
    import random
    array = []
    for i in range(0, quantity):
        array.insert(i, int(random.randrange(minimum,maximum)))
    return array

def NonRepeatingElements(array):
    NREArray = []
    for i in range(0, len(array)):
        if array.count(array[i]) == 1: NREArray.append(array[i])
    return NREArray

print('Здравствуте!')
number = int(input('Сколько чисел хотите видеть в списке? '))

newArray = FillRandomArray(number, 1, 9)

print(f"Получили массив: {newArray}")

print(f'Вот числа, которые не повторяются в текущем списке: {NonRepeatingElements(newArray)}')