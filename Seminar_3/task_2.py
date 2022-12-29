#Напишите программу, 
#которая найдёт произведение пар чисел списка. 
#Парой считаем первый и последний элемент, 
#второй и предпоследний и т.д.

#Пример:

#- [2, 3, 4, 5, 6] => [12, 15, 16];
#- [2, 3, 5, 6] => [12, 15]

def FillRandomArray(quantity, minimum, maximum):
    import random
    array = []
    for i in range(0, quantity):
        array.insert(i, int(random.randrange(minimum,maximum)))
    return array

def ProductPairsNumbers(array):
    productArray = []
    for i in range(0, len(array)):
        if i == int(0 + ((len(array)-1)/2)) and len(array)%2 > 0:
            productArray.append(array[i] * array[i])
            return productArray
        elif i == int(0 + ((len(array)-1)/2)) and len(array)%2 == 0:
            productArray.append(array[i] * array[len(array)-i-1])
            return productArray
        else:
            productArray.append(array[i] * array[len(array)-i-1])
    return productArray

print('Здравствуте!')
number = int(input('Сколько чисел хотите видеть в списке? '))

newArray = FillRandomArray(number, 1, 9)

print(f"Получили массив: {newArray}")

prodArray = ProductPairsNumbers(newArray)
print(prodArray)