#Создайте программу для игры с конфетами человек против человека. 
#Реализовать игру игрока против игрока в терминале. Игроки ходят друг за другом, 
#вписывая желаемое количество конфет. 
#Первый ход определяется жеребьёвкой. 
#В конце вывести игрока, который победил

def WhoFirst(counter):
    import random
    first = int(random.randrange(0, counter))
    return first

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

print('Приветствую вас, игроки!')
playerOne = str(input('Как зовут первого игрока? '))
playerTwo = str(input('Как зовут второго игрока? '))

candy = int(input('Сколько у вас конфет? '))

if RivalCandies(candy, playerOne, playerTwo) == 1: print(f'Победил {playerOne}, поздравляем!')
else: print(f'Победил {playerTwo}, поздравляем!')