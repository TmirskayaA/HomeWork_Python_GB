#Задайте список из нескольких чисел. 
#Напишите программу, 
#которая найдёт сумму элементов списка, 
#стоящих на нечётной позиции.

#Пример:

# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

def FillRandomArray(quantity, minimum, maximum):
    import random
    array = []
    for i in range(0, quantity):
        array.insert(i, int(random.randrange(minimum,maximum)))
    return array

def OddPositions(array):
    oddArray = []
    for i in range(0, len(array)):
        if (i + 1) % 2 > 0: oddArray.append(f'{i+1}->{array[i]}')
    return oddArray

def SumOddPositions(array):
    sum = 0
    for i in range(0, len(array)):
        if (i + 1) % 2 > 0: sum += array[i]
    return sum

print('Здравствуте!')
number = int(input('Сколько чисел хотите видеть в списке? '))

newArray = FillRandomArray(number, 1, 9)

print(f"Получили массив: {newArray}")

oddPosArray = OddPositions(newArray)

print("Нечётные позиции заняты следующими элементами:")
for i in range(0, len(oddPosArray)):
    print(oddPosArray[i])

print(f"Сумма этих элементов = {SumOddPositions(newArray)}!")

