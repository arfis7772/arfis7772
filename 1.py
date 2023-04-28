from random import *

maps_gamer = [[0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0],]

maps_bot = [[0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],]

def draw():
    for num, i  in enumerate(maps_gamer):
        for j in i:
            print(j, end=' ')
        print('|', end=' ')
        for j in maps_bot[num55]:
            print(j, end=' ')
        print('')
 
draw()

atack = int(input('введите номер клетки по горезонтали а затем по вертикали:'))
