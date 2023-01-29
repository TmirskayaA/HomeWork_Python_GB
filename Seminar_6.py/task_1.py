#Заполните массив элементами арифметической прогрессии. 
#Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
#Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
#Каждое число вводится с новой строки.
#Ввод: 7 2 5
#Вывод: 7 9 11 13 15

def NextElement(element, counter, difference):
    return element + (counter - 1) * difference

def ArithmeticProgression(element, difference, quantity):
    resultArray = [NextElement(element, i, difference) for i in range(1, quantity+1)]
    return resultArray

print('\nЗдравствуйте!\n')

firstElement = int(input('Введите первый элемент: '))
step = int(input('Введите значение шага: '))
count = int(input('Задайте число элементов в результате: '))

print(f'\nРезультат: {ArithmeticProgression(firstElement, step, count)}')