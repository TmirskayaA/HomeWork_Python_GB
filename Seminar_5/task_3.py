#Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
#Входные данные:
#111112222334445
#Выходные данные:
#5142233415
#Также должно работать и для букв:
#Входные данные:
#AAAAAAFDDCCCCCCCAEEEEEEEEEEEEEEEEE
#Выходные данные:
#6A1F2D7C1A17E

def FromArrayToString(array):
    string = array[0]
    for i in range(1, len(array)):
        string = string + array[i]
    return string

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

print('Здравствуйте!')
string = str(input('Введите набор символов: '))

string = StringCompression(string)

print(f'Вот что получилось после сжатия: {string}')

file = open('file(3inS5).txt', 'a')
file.write(string)
file.close()

answer = str(input('Восстанавливаем данные? (Да/Нет): '))
if answer == 'Да':
    file = open('file(3inS5).txt', 'r')
    string = file.readline()
    file.close()
    print(f'Восстановили данные: {StringRecovery(string)}')

answer = str(input('Отчищаем файл? Напишите \"Да\" или \"Нет\": '))
while answer != 'Да' and answer != 'Нет':
    answer = str(input('Вы написали что-то не то. Напишите \"Да\" или \"Нет\": '))
if answer == 'Да': 
    file = open('file(3inS5).txt', 'w')
    file.close()
else: exit()


    


