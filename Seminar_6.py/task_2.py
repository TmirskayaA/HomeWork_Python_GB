#Определить индексы элементов массива (списка), 
#значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

#Минимум: 5
#Максимум 15
#Ввод:  [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
#         0  1  2  3   4   5  6  7   8   9  10 11 12  13 14  15  16 17  18 19
#Вывод: [1, 9, 13, 14, 19]

def WithinTheInterval(array, minimum, maximum):
    resultArray = [i for i in range(0, len(array)) if array[i] >= minimum and array[i] <= maximum]
    return resultArray

print('\nЗдравствуйте!\n')

string = input('Нашитите элементы массива по порядку: ')
arrayDigit = [int(string[i]) for i in range(0,len(string))]
bordermin = int(input('Введите значение минимума: '))
bordermax = int(input('Введите значение максимума: '))

if len(WithinTheInterval(arrayDigit, bordermin, bordermax)) == 0: print('\nТаких чисел в массиве нет!')
else: print(f'\nНужные элементы находятся на следующих позициях: {WithinTheInterval(arrayDigit, bordermin, bordermax)}')