from data import enemies, player, shop
from time import sleep
from random import randint


def fight(current_enemy):
    round = randint(1, 2)
    enemy = enemies[current_enemy]
    enemy_hp = enemies[current_enemy]['hp']
    print(f'Противник - {enemy["name"]}: {enemy["script"]}')
    input('Enter чтобы продолжить')
    print()
    while player['hp'] > 0 and enemy_hp > 0:
        if round % 2 == 1:
            print(f'{player["name"]} атакует {enemy["name"]}.')
            enemy_hp -= player['attack']
            sleep(1)
            print(f'''{player['name']} - {player['hp']}
    {enemy['name']} - {enemy_hp}''')
            print()
            sleep(1)
        else:
            print(f'{enemy["name"]} атакует {player["name"]}.')
            player['hp'] -= enemy['attack']
            sleep(1)
            print(f'''{player['name']} - {player['hp']}
    {enemy['name']} - {enemy_hp}''')
            print()
            sleep(1)
        round += 1

    if player['hp'] > 0:
        print(f'Противник - {enemy["name"]}: {enemy["win"]}')
    else:
        print(f'Противник - {enemy["name"]}: {enemy["loss"]}')  


def display_player():
    print(f'Игрок - {player["name"]}')
    print(f'Величина атаки - {player["attack"]}')
    print(f'Показатели брони - {player["armor"]}')
    print(f'Здоровье - {player["hp"]}')
    print()

def display_ememy(current_enemy):
    enemy = enemies[current_enemy]
    print(f'Противник - {enemy["name"]}')
    print(f'Величина атаки - {enemy["attack"]}')
    print(f'Здоровье - {enemy["hp"]}')
    print()

def display_inventory():
    if len (player['inventory']) == 0:
        print("Инвентарь пустой")
    else:
        for item in player['inventory']:
            print(item["name"])
            if 'attack' in item.keys():
                print(f"Бонус к атаке: {item['attack']}")
            if 'armor' in item.keys():
                print(f"Бонус к броне: {item['armor']}")
            if 'hp' in item.keys():
                print(f"Бонус к здоровью: {item['hp']}")
        print("Одноразовое использование" if item['single_time_use'] else 'Можно экипировать')
        user_choice = input('Хотите ли вы что нибудь использовать?(да/нет)')
        if user_choice == "да":
                user_choice = int(input("Введите номер предмета(1, 2, 3)"))
                if user_choice > len(player['inventory']):
                    user_choice = len(player['inventory'])
                if user_choice < 1:
                    user_choice = 1
                user_choice -= 1
                if "attack" in player["inventory"][user_choice]:
                    if "attack" in player["inventory"][user_choice]:
                        player["attack"] += player["inventory"][user_choice]["attack"]
                if "armor" in player["inventory"][user_choice]:
                        player["armor"] -= player["inventory"][user_choice]["armor"]
                if "hp" in player["inventory"][user_choice]:
                        player["hp"] += player["inventory"][user_choice]["hp"]
                if player["inventory"][user_choice]["single_time_use"]:
                    del player["inventory"][user_choice]

def training(training_type):
    for i in range(0, 101, 20):
        print(f"Тренировка завершена на {i}%")
        sleep(1)
    if training_type == 0: # На здоровье
        player ["armor"] -= 0.05
        print(f'Тренировка окончена: теперь ваша броня поглощает {(1-player["attack"])*100}%')
    elif training_type == 1: # На защиту
        player['attack'] += 2
        print(f'Тренировка окончена: теперь ваша атака равна {player["attack"]}')

def display_shop():
    for item in shop:
        print(item["name"])
        if 'attack' in item.keys():
            print(f"Бонус к атаке: {item['attack']}")
        if 'armor' in item.keys():
            print(f"Бонус к броне: {item['armor']}")
        if 'hp' in item.keys():
            print(f"Бонус к здоровью: {item['hp']}")
            print("Одноразовое использование" if item['single_time_use'] else 'Можно экипировать')
            print(f"Цена {item['price']}")
    user_choice = input('Хотите ли вы что нибудь использовать?(да/нет)')
    if user_choice == "да":
        user_choice = int(input("Введите номер предмета(1, 2, 3)"))
        if user_choice > len(shop):
            user_choice = len(shop)
        if user_choice < 1:
            user_choice = 1
        user_choice -= 1
        if shop[user_choice]["price"] < player["money"]:
            player["money"] -= shop[user_choice]["price"]
            player["inventory"].append(shop[user_choice])
        else:
            print("Недостаточно средств...")