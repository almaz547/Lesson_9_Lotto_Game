from classis import *





len_players = 0                            # Количество  играков
list_players = []                             # Список игрок + тип
type_player = None                      # Тип игрока

while len_players == 0:
    try:
        len_players = int(input('Введите количество игроков:  '))
    except ValueError:
        print('Введите число ! ! !')
for i in range(len_players):
    name = input(f'Введите имя игрока {i + 1} :  ')
    while type_player not in (0, 1):
        try:
            type_player = int(input(f'Введите тип игрока {name} :  0  если компютер,  1   если человек:  '))
        except ValueError:
            print('Введите число ! ! !')
    list_players.append(Card((i + 1, name, type_player)))
    type_player = None
bag = Bag()                                                        # Создали имя для класса мешок
x = 1
motion = input('Зделать ход нажмите   Enter  ')
while motion == '':
    bag_mot = bag.out_tank()                                      # Достать из мешка один бачонок и обозвали его
    print('*' * 31)
    print(f'Ход номер   {x}')
    print('*' * 19)
    for gamer in list_players:
        gamer.fill_cart()                                                # Заполняем  карточку игрока
        if gamer.delete_number(bag_mot):
            if not gamer.name[2]:
                print(f'Бачонок №  {bag_mot} из карты компа  {gamer.name[0]}.{gamer.name[1]}   Удален !')
            else:
                choice_bag = input(
                    f'Игрок  {gamer.name[0]}.{gamer.name[1]}: Если номер***   {bag_mot}   *** есть, для удаления нажмите:  u   , если номера нет нажмите:   n  ')
                if choice_bag == 'u':
                    print(f'Бачонок №  {bag_mot} из карты  {gamer.name[0]}.{gamer.name[1]}   Удален !')
                else:
                    print(f'Вы   {gamer.name[0]}.{gamer.name[1]}   проиграли ! Бачонок №  {bag_mot} в вашей карте есть !')
                    list_players.remove(gamer)
        else:
            if gamer.name[2]:
                choice_bag = input(
                    f'Игрок  {gamer.name[0]}.{gamer.name[1]}: Если номер***   {bag_mot}   *** есть, для удаления нажмите:  u   , если номера нет нажмите:   n  ')
                if choice_bag == 'n':
                    print(f'Все верно! Бачонка №  {bag_mot}  в вашей  карте   {gamer.name[0]}.{gamer.name[1]}    нет !')
                else:
                    print(f'Не правильный  выбор ! Вы    {gamer.name[0]}.{gamer.name[1]}    проиграли !')
                    list_players.remove(gamer)
            else:
                print(f'Бачонка №  {bag_mot}  в  карте компа   {gamer.name[0]}.{gamer.name[1]}    нет')

    x += 1                                                                # Переключаем счетчик хода
    motion = input('Зделать ход нажмите    Enter  ')
print("Стоп  Стоп")

'''
Следующий вариант думаю будет прогрессивнее, с большим количеством использования классов.
'''

