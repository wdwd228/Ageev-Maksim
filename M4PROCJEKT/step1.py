from data import player, enemies
from helpers import fight, display_player, display_ememy, training, display_inventory, display_shop

name = input('Введи своё имя, путник: ')
player['name'] = name
current_enemy = 0

while True:
    action = input('''Введите действие:
1 - В бой!
2 - Показать информацию об игроке
3 - Показать информацию о противнике
4 - Начать тренировку на здоровье
5 - Начать тренировку на броню
6 - Открыть инвентарь
7 - Зайти в магазин Выбрать: ''')
    if action == "1":
        fight(current_enemy)
    elif action == "2":
        display_player()
    elif action == "3":
        display_ememy(current_enemy)
    elif action == "4":
        training(0)
    elif action == "5":
        training(1)
    elif action == "6":
        display_inventory()
    elif action == "7":
        display_shop()
