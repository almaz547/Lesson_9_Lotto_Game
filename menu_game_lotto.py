from classis import *




while True:
    print('Меню игры')
    print('Выберите варианты игры')
    print('1. Один игрок и компютер')
    print('2. Два играка')
    print('3. Два компютера')

    choice = input('Выберите пункт меню: ')

    if choice == '1':
        nam = input('Введите имя игрока: ')
        name = Card()
        numbers_card_name = name.choice_numbers_card()
        name.choice_position()

        robot = Card()                                                       # Создали  имя  робота
        robot.choice_numbers_card()                                    # Создали  15 цифр для карточки
        robot.choice_position()                                   # Создали 15 номеров для позиций  заполнения карточки

        game = Bag()                                        # Создали имя для класса мешок
        game.fill_bag()                                     # Заколнили мешок для игры

        print('-' * 40)
        print('Ваши карточки -- начинаим играть')
        print('-' * 40)
        print(f'Карточка   ---   {nam}   ---  ')
        print('-' * 40)
        name.fill_cart(f'{nam}')                            # Заполняем новую карту игрока 1
        print('-' * 40)
        print('Карточка   ---   robot   ---  ')
        print('-' * 40)
        robot.fill_cart('robot')                         # Заполняем новую карту робота

        motion = input('Зделать ход нажмите  Enter   ')
        print('-' * 55)
        x = 1
        while motion == '':
            print('*' * 19)
            print(f'Ход номер {x}')
            print('*' * 31)
            bag = game.out_tank()                                # Достать из мешка один бачонок
            print(f'Бачонок номер:    {bag}   !!!')
            print('-' * 40)
            print(f'Выбор  игрока ---  {nam}  --- ')
            print('-' * 40)
            choice_bag = input(f'Если такой номер есть, для удаления нажмите:  u   , если номера нет нажмите:   n  ')
            print('-' * 25)
            if bag in numbers_card_name:
                if choice_bag == 'u':
                    if name.delete_number(bag, f'{nam}') == True:
                        print(f'Бачонок {bag} из карты  {nam}   Удален !')
                        print('-' * 40)
                    elif name.delete_number(bag, f'{nam}') == False:
                        print(f'Программа ошиблась! и баченка {bag}  на карте   {nam}   все таки нет.')
                else:
                    print(f'Вы   {nam}   проиграли ! Бачонок {bag} в вашей карте есть !')
                    break
            else:
                if choice_bag == 'n':
                    if name.delete_number(bag, f'{nam}') == False:
                        print(f'Все верно! Бачонка {bag}  в вашей карте   {nam}   нет !')
                        print('-' * 40)
                    elif name.delete_number(bag, f'{nam}') == True:
                        print(f'Программа ощиблась и баченок {bag}  с карты   {nam}   все таки был и Удален !')
                else:
                    print(f'Не правильный выбор ! Вы   {nam}    проиграли !')
                    break
            name.fill_cart(f'{nam}')                         # Заполняем карту игрока после удаления или нет цифры с бачонка

            if robot.delete_number(bag, 'robot') == True:     # Удаляем, если есть, бачонок из списка номеров одного игрока
                print(f'Бачонок {bag} с карты  robot   Удален !')
                print('-' * 40)
            elif robot.delete_number(bag, 'robot') == False:         # А если нет: принт нет
                print(f'Бачонка {bag} в карте  robot   нет !')
                print('-' * 40)
            robot.fill_cart('robot')                            # Заполняем карту 2
            x += 1
            motion = input('Зделать ход нажмите   Enter   ')
            print('-' * 25)


    elif choice == '2':

        gmer_1 = input('Введите имя первого игрока:  ')
        gamer_1 = Card()
        numbers_card_gamer_1 = gamer_1.choice_numbers_card()
        gamer_1.choice_position()

        gmer_2 = input('Введите имя второго игрока:   ')
        gamer_2 = Card()                                             # Создали  для второго играка переменную
        numbers_card_gamer_2 = gamer_2.choice_numbers_card()  # Создали  15 цифр для карточки и записоли в переменную для проверки есть ли там цифра
        gamer_2.choice_position()                               # Создали 15 номеров для позиций  заполнения карточки

        game = Bag()                                                          # Создали имя для класса мешок
        game.fill_bag()                                                   # Заполнили мешок для игры

        print('-' * 40)
        print('Ваши карточки -- начинаим играть')
        print('-' * 40)
        print(f'Карточка   ---   {gmer_1}   ---  ')
        print('-' * 40)
        gamer_1.fill_cart(f'{gmer_1}')                                   # Заполняем новую карту игрока 1
        print('-' * 40)
        print(f'Карточка   ---   {gmer_2}   ---  ')
        print('-' * 40)
        gamer_2.fill_cart(gmer_2)                                       # Заполняем новую карту игрока 2

        motion = input('Зделать ход нажмите   Enter   ')
        print('-' * 55)
        x = 1
        while motion == '':
            print('*' * 19)
            print(f'Ход номер {x}')
            x += 1
            print('*' * 31)
            bag = game.out_tank()                                # Достать из мешка один бачонок
            print(f'Бачонок номер:    {bag}   !!!')
            print('-' * 25)
            print(f'Выбор для  игрока   ---  {gmer_1}  ---')
            print('-' * 25)
            choice_bag = input(f'Если такой номер есть, для удаления нажмите:  u   , если номера нет нажмите:   n  ')
            print('-' * 25)

            if bag in numbers_card_gamer_1:
                if choice_bag == 'u':
                    if gamer_1.delete_number(bag, f'{gmer_1}') == True:
                        print(f'Бачонок {bag} из карты  {gmer_1}   Удален !')
                    elif gamer_1.delete_number(bag, f'{gmer_1}') == False:
                        print(f'Программа ошиблась! и баченка {bag}  в карточке   {gmer_1}   все таки нет.')
                else:
                    print(f'Вы   {gmer_1}   проиграли ! Бачонок {bag} в вашей карте есть !')
                    break
            else:
                if choice_bag == 'n':
                    if gamer_1.delete_number(bag, f'{gmer_1}') == False:
                        print(f'Все верно! Бачонка {bag}  в вашей  карте   {gmer_1}    нет !')
                    elif gamer_1.delete_number(bag, f'{gmer_1}') == True:
                        print(f'Программа ощиблась и баченок {bag}   с  карты   {gmer_1}   все таки   Удален !')
                else:
                    print(f'Не правильный  выбор ! Вы    {gmer_1}    проиграли !')
                    break

            print('-' * 25)
            print(f'Выбор для  игрока   ---  {gmer_2}  ---')
            print('-' * 25)
            choice_bag = input(f'Если такой номер есть, для удаления нажмите:  u   , если номера нет нажмите:   n  ')
            print('-' * 25)

            if bag in numbers_card_gamer_2:
                if choice_bag == 'u':
                    if gamer_2.delete_number(bag, f'{gmer_2}') == True:
                        print(f'Бачонок  {bag}  из карты   {gmer_2}   Удален !')
                    elif gamer_2.delete_number(bag, f'{gmer_2}') == False:
                        print(f'Программа ошиблась! и баченка {bag}   в карте   {gmer_2}   все таки нет.')
                else:
                    print(f'Вы   {gmer_2}   проиграли ! Бачонок {bag} в вашей карте есть !')
                    break
            else:
                if choice_bag == 'n':
                    if gamer_2.delete_number(bag, f'{gmer_2}') == False:
                        print(f'Все верно! Бачонка {bag}  в вашей карте   {gmer_2}   нет !')
                    elif gamer_2.delete_number(bag, f'{gmer_2}') == True:
                        print(f'Программа ощиблась и баченок {bag}  с карты   {gmer_2}   все таки был и Удален !')
                else:
                    print(f'Не правильный выбор ! Вы   {gmer_2}   проиграли !')
                    break
            print('-' * 40)
            print(f'Карточка   ---   {gmer_1}   ---  ')
            print('-' * 40)
            gamer_1.fill_cart(f'{gmer_1}')  # Заполняем карту первого игрока после удаления или нет цифры  бачонка
            print('-' * 40)
            print(f'Карточка   ---   {gmer_2}   ---  ')
            print('-' * 40)
            gamer_2.fill_cart(f'{gmer_2}')  # Заполняем карту второго игрока после удаления или нет цифры  бачонка

    elif choice == '3':
        robot_1 = Card()                               # Создали первое имя
        robot_1.choice_numbers_card()                  # Создали для первого имени  15 цифр для карточки
        robot_1.choice_position()                      # Создали для первого имени позиций для заполнения

        robot_2 = Card()                                # Создали второе имя
        robot_2.choice_numbers_card()                   # Создали для второго 15 цифр для карточки
        robot_2.choice_position()                       # Создали для второго номера позиций для заполнения

        game = Bag()                                   # Создали имя для класса мешок
        game.fill_bag()                                # Заколнили мешок для игры
        print('-' * 40)
        print('Ваши карточки --- начинаим играть')
        print('-' * 40)
        print('Карточка   ---   robot_1   ---  ')
        print('-' * 40)
        robot_1.fill_cart('robot_1')                   # Заполняем новую карту 1
        print('Карточка   ---   robot_2   ---  ')
        print('-' * 40)
        robot_2.fill_cart('robot_2')                   # Заполняем новую карту 2

        motion = input('Зделать ход нажмите   Enter  ')
        print('-' * 40)
        x = 1
        while motion == '':
            print('*' * 31)
            print(f'Ход номер {x}')
            print('*' * 19)
            bag = game.out_tank()                                     # Достать из мешка один бачонок и обозвали его
            print(f'Бачонок номер:    {bag}   !!!')
            print('-' * 25)

            if robot_1.delete_number(bag, name='robot_1') == True:   # Удаляем, если есть, бачонок из списка номеров одного игрока
                print(f'Бачонок {bag} из карты  robot_1   Удален !')
            elif robot_1.delete_number(bag, name='robob_1') == False:
                print(f'Бачонка {bag} в карте  robot_1   нет !')
            robot_1.fill_cart('robot_1')                              # Заполняем карту 1

            if robot_2.delete_number(bag, 'robot_2') == True:     # Удаляем, если есть, бачонок из списка номеров второго игрока
                print(f'Бачонок {bag} из карты  robot_2   Удален !')
            elif robot_2.delete_number(bag, 'robot_2') == False:
                print(f'Бачонка {bag} в карте  robot_2   нет !')
            robot_2.fill_cart('robot_2')                            # Заполняем карту 2
            x += 1                                               # Переключаем счетчик хода
            motion = input('Зделать ход нажмите    Enter  ')


    else:
        print('Неправильный пункт меню')

