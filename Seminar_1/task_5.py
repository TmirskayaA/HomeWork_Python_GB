#Напишите программу, 
#которая принимает на вход 
#координаты двух точек 
#и находит расстояние между ними 
#в 2D пространстве.

#Пример:

#A (3,6); B (2,1) -> 5,09
#A (7,-5); B (1,-1) -> 7,21

print('Здравствуте!')
xa = float(input('Какие координаты у точки А на оси X? '))
ya = float(input('Какие координаты у точки А на оси Y? '))
xb = float(input('Какие координаты у точки B на оси X? '))
yb = float(input('Какие координаты у точки А на оси Y? '))

import math

print(f'Растояние между точкой A до точки B = {round(math.sqrt((xa-xb)**2+(ya-yb)**2), 2)}!')