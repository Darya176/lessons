import game
while True:
    start = input('Чтобы начать игру, нажмите "Enter", чтобы завершить игру введите "0": ')

    if start == '0':
        print('Игра завершена')
        break
    else:
        game.main(start)
