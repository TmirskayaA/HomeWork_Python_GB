#Задайте список из n чисел 
#последовательности $(1+\frac 1 n)^n$ 
#и выведите на экран их сумму.

#Пример:

#Для n=4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44}

print('Здравствуте!')
number = int(input('Напишите число: '))

dictionary = {i: round((1 + 1 / i)**i, 2) for i in range(1, number+1)}

summ = 0

for i in range(1, number+1):
    summ += dictionary.get(i)

print(f'Словарь из {number} чисел:')
print(dictionary)
print(f'Сумма чисел: {summ}.')

