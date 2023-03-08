game_list = []
while True:
    game = input('Введите название игры: ')
    if game != "0":
        if game not in game_list:
            game_list.append(game)
            print('Игра добавлена')
        else:
            print('Игра уже существует')
    else:
        print('Список сформирован')
        break
game_list.sort()
print(game_list)