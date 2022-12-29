#Определение типа данных
def DefiningDataType(type):
    if type == 'числовой': return int
    elif type == 'текстовый': return str
    elif type == 'вещественный': return float
    elif type == 'список': return list
    elif type == 'логический': return bool
    else: return 'error'

#Заполнение массива (кол-во элементов, тип элементов)
def FillArray(quantity, type):
    array = []
    for i in range(0, quantity):
        element = type(input(f'Задайте {i+1} элемент: '))
        array.append(element)
    return array

#Наличие цифры в массиве
def HaveDigit(array):
    for i in range(0, len(array)):
        if array[i].isdigit(): return True

#Индекс первого повторения элемента в массиве
def FirstRepeatIndex(array, element):
    replay = 0
    index = -1
    for i in range(0, len(array)):
        if array[i] == element:
            replay += 1
            if replay == 2:
                index = i
    return index

#Массив элементов на нечётных позициях (*индекс*->*элемент*)
def OddPositions(array):
    oddArray = []
    for i in range(0, len(array)):
        if (i + 1) % 2 > 0: oddArray.append(f'{i+1}->{array[i]}')
    return oddArray

#Сумма элементов на нечётных позициях
def SumOddPositions(array):
    sum = 0
    for i in range(0, len(array)):
        if (i + 1) % 2 > 0: sum += array[i]
    return sum

#Произведение пар в массиве (пары: начало - конец и т.д.)
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

#Разница между максимальным и минимальным значением в дроби в массиве
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

#Перевод десятичного числа в двоичное
def ToBinary(digit):
    max = digit
    while digit != 0:
        if digit == max: binary = str(digit % 2)
        else: binary = str(digit % 2) + binary
        digit //= 2
    return binary

#Массив простых множителей числа
def MultiplierArray(digit):
    array = []
    i = 2
    while i <= digit:
        if digit % i == 0:
            array.append(i)
            digit //= i
            i = 2
        else: i += 1
    return array

#Массив элементов, которые не повтояются в исходном массиве
def NonRepeatingElements(array):
    NREArray = []
    for i in range(0, len(array)):
        if array.count(array[i]) == 1: NREArray.append(array[i])
    return NREArray