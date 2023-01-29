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

#Рандомный выбор кто будет первым из N игроков.
def WhoFirst(counter):
    import random
    first = int(random.randrange(0, counter))
    return first

#Игра в конфеты.
def RivalCandies(counter, nameOne, nameTwo):

    print('Взять можно не больше 28 конфет. Возвращать конфеты в кучку тоже нельзя.')

    queue = WhoFirst(2)

    if queue == 1: print(f'Первым ходит {nameOne}!')
    else: print(f'Первым ходит {nameTwo}!')

    while counter != 0:
        if queue == 1:
            motion = int(input(f'{nameOne}, cколько конфет из {counter} возьмёшь? '))
            if motion > 28: print('Не жадничай! Больше 28 нельзя. За нарушение правил у тебя -1 ход.')
            elif motion < 0: print('Возвращать конфеты нельзя! Раз взял, значит ешь. За нарушение правил у тебя -1 ход.')
            else: counter = counter - motion
        else: 
            motion = int(input(f'{nameTwo}, cколько конфет из {counter} возьмёшь? '))
            if motion > 28: print('Не жадничай! Больше 28 нельзя. За нарушение правил у тебя -1 ход.')
            elif motion < 0: print('Возвращать конфеты нельзя! Раз взял, значит ешь. За нарушение правил у тебя -1 ход.')
            else: counter = counter - motion
        last = queue
        if queue == 1: queue = 2
        else: queue = 1
    return last

#Переводим массив в строку.
def FromArrayToString(array):
    string = array[0]
    for i in range(1, len(array)):
        string = string + " " + array[i]
    return string

#Сжимаем строку *прим*111122233 в формат *прим*413223 (работает с буквами).
def StringCompression(string):
    array = []
    cycle = 0

    for i in range(0, len(string)):
        if i != cycle: continue
        else:
            object = string[i]
            counter = 0
            for j in range(0, len(string)):
                if string[j] == object:
                    counter += + 1
        endObject = str(counter)+object
        array.append(endObject)
        cycle += counter
    
    return FromArrayToString(array)

#Восстанавливает строку *прим*413223 в вид *прим*111122233.
def StringRecovery(string):
    array = []
    object = None

    for i in range(0, len(string)-1):
        if i % 2 != 0: continue
        else:
            strObject =  str(string[i+1])
            result = strObject*int(string[i])
            array.append(result)
            object = string[i+1]
    
    return FromArrayToString(array)

#Расчитываем следующий элемент арифметической прогрессии для task_1 S6
def NextElement(element, counter, difference):
    return element + (counter - 1) * difference

#Добавляем следующий элемент арифметической прогрессии в массив для task_1 S6
def ArithmeticProgression(element, difference, quantity):
    resultArray = [NextElement(element, i, difference) for i in range(1, quantity+1)]
    return resultArray

#Фильтруем массив по значениям от min до max и оставляем в списке только подходящие элементы.
def WithinTheInterval(array, minimum, maximum):
    resultArray = [i for i in range(0, len(array)) if array[i] >= minimum and array[i] <= maximum]
    return resultArray

#Возведение число в степень с помощью рекурсии.
def Exponentiation(digit, degree):
    if (degree == 1): return (digit)
    else: return (digit * Exponentiation(digit, degree - 1))