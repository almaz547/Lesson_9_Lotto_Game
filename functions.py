from classis import Player, Robot, Card


def huw_much_players():                        # Определяем количество игроков
    len_players = 0
    while len_players == 0:
        try:
            len_players = int(input('Введите количество игроков:  '))
        except ValueError:
            print('Введите число ! ! !')
    return len_players



def number_name_type_player(len_players):  # Вводим номер имя и тип каждого игрока и присваеваем класс игрока человек или робот                                    # Тип игрока
    list_players = []
    for i in range(len_players):
        type_player = None
        name = input(f'Введите имя игрока {i + 1} :  ')
        while type_player not in (0, 1):
            try:
                type_player = int(input(f'Введите тип игрока {name} :  0  если компютер,  1   если человек:  '))
            except ValueError:
                print('Введите число  0  или  1  ! ! !')
        player = Player(i + 1, name, type_player) if type_player else Robot(i + 1, name, type_player)
        list_players.append(player)
    return list_players


def comparison_remove_numbers(list_players):            # Анализ игры по закрытым номерам
    list_players.sort(reverse=True)        # Сортеруем игроков по количеству зачеркнутых номеров в порядке убывания
    for player in list_players:
        print(f'Закрытых номеров: ---  {player.card.remove_number}  --- у {player} ')



