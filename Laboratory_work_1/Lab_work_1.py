# работа выполнена Броварник Глебом
# Вариант 4

from time import sleep
import os

RED = '\u001b[41m' 
WHITE = '\u001b[47m'
BLACK = '\u001b[40m'
GREEN = '\u001b[42m'

RESET = '\u001b[0m' 

colors = [220, 167, 130, 215] # набор цветов

def polish_flag(size): # размер
    height = size
    width = 4 * size
    for i in range(height//2):
        print(f"{WHITE}{width * " "}{RESET}")
    for i in range(height//2):
        print(f"{RED}{width * " "}{RESET}")

def brick_pattern(row, column, color): # количество строк, столбцов и цвет
    width = 12
    height = 4
    for c in range(column):
        for line in range(1, height+1):
            if line == 1 or line == 3:
                print(f"\x1B[48;5;{color}m{width*" "}{RESET}"*row)
            elif 1 < line < 3:
                print(f"{" "*(width-2)}\x1B[48;5;{color}m  {RESET}"*row)
            else:
                print(f"{" "*(width//2-1)}\x1B[48;5;{color}m  {RESET}{" "*(width//2-1)}"*row)


def brick_animation(colors): # список цветов
    color_index = 0
    while True:
        for index_change in range(len(colors)):
            brick_pattern(5, 1, colors[(color_index+index_change)%len(colors)])
        sleep(0.7)
        os.system('cls' if os.name == 'nt' else 'clear')
        color_index += 1


def sequence():
    file = open('sequence.txt', 'r')
    numbers = []
    for line in file:
        num = abs(float(line))
        numbers.append(num)
    file.close()
    first_125, second_125 = sum(numbers[:125])/125, sum(numbers[125:])/125
    print(f'{GREEN}{' '*int(first_125*7)}{RESET} {round(first_125 / (first_125 + second_125) * 100, 2)}%')
    print(f'{RED}{' '*int(second_125*7)}{RESET} {round(second_125 / (first_125 + second_125) * 100, 2)}%')


def function_sqrt(size_x): #длина функции вдоль оси X
    y = []
    offset = size_x #смещение отмечения графика
    for x in range(size_x, -1, -1):
        y.append(round(x**0.5))
    row = list(set(y))
    row.sort(reverse=True)
    print("y"," "*5, "y=x**0.5")
    for line in row:
        c = y.count(line)
        print(line, f"{BLACK}{" "*(offset-c+1)}{GREEN}{" "*c}{BLACK}{" "*(size_x-offset)}{RESET}")
        offset = offset-c

# polish_flag(8) # флаг

brick_pattern(7, 3, 167) # узор

# brick_animation(colors) # анимация

# sequence() # диаграмма

# function_sqrt(40) # функция