from classis import *
from functions import *


len_players = huw_much_players()
list_players = number_name_type_player(len_players)
game = True
bag = Bag()                                                        # Создали имя для класса мешок
while game:
    motion = input('Зделать ход нажмите   Enter  ')
    bag_mot = bag.out_tank()                         # Достать из мешка один бачонок и обозвали его
    print('*' * 31)
    print(f'Ход номер   {bag.numer_motion}')
    print('*' * 19)
    for player in list_players:
        print(player.card.fill_cart())                                                # Заполняем  карточку игрока
        if player.type_player:
            request = input(f'Игрок  {player.num_player}.{player.name}: Если  номер ***   {bag_mot}   *** есть, для  удаления  нажмите: u, если  номера  нет  нажмите: n ')
        else:
            request = None
        player.card.delete_number(bag_mot)                          # Удаляет номер из списка номеров карточки
        delete, info = player.action_player(bag_mot, request)                # Действия игрока
        print(info)
        if delete:
            list_players.remove(player)
            print(f'Карточка {player.num_player}.{player.name}  проиграла и удалена')
        if player.card.victory:
            print(f'Карточка  {player.card.num_player}  Игрока  {player.card.name} Победитель ! ! !')
            print('Игра  окончена !')
            game = False














