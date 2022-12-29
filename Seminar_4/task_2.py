#Задайте натуральное число N. 
#Напишите программу, 
#которая составит список простых множителей числа N.

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

print('Здравствуте!')
number = int(input("Напишите число: "))

print(f"Простые множители числа {number} = {MultiplierArray(number)}")