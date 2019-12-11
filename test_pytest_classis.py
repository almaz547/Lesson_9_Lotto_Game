from classis import *



class TestBag:
    def test__init__(self):
        bag = Bag()
        assert bag.game_bag == list(range(1, 91))
        assert bag.numer_motion == 0

    def test_out_tank(self):
        bag = Bag()
        if bag.game_bag:
            assert bag.game_bag != []
            assert bag.numer_motion == 0
            tank = random.sample(bag.game_bag, 1)
            for el in tank:
                tank = el
            assert tank in bag.game_bag
            bag.game_bag.remove(tank)
            assert tank not in bag.game_bag
            el = tank
            assert not el in bag.game_bag

            result = bag.out_tank()
            assert result in range(1, 91) and result not in bag.game_bag


class TestCard():

    def test___init__(self):
        card = Card(1, 'max')
        assert card.count_number == range(1, 91)
        assert card.len_line == range(9)
        assert card.num_player == 1
        assert card.name == 'max'
        assert card.is_there_barrel == 0
        assert card.victory == False

        assert len(card.numbers) == 15
        number_max = 0
        for number in card.numbers:
            assert number in range(1, 91)
            assert not number not in range(1, 91)
            assert number > number_max
            if number > number_max:
                number_max = number

        assert len(card.list_full_position) == 3
        for line in card.list_full_position:
            assert len(line) == 5
            for number in line:
                assert number in card.len_line
                assert not number not in card.len_line

    def test_delete_number(self):
        card = Card(1, 'max')
        bag_class = Bag()
        for i in range(90):
            bag = bag_class.out_tank()
            if bag in card.numbers:
                assert bag in card.numbers
                x = card.numbers.index(bag)
                card.delete_number(bag)
                assert bag not in bag_class.game_bag
                assert card.numbers[x] == None
                assert card.is_there_barrel == True
            else:
                assert bag not in bag_class.game_bag
                card.delete_number(bag)
                assert card.is_there_barrel == False

    def test_fill_cart(self):
        card = Card(num_player=1, name='max')
        bag_class = Bag()
        for i in range(90):
            bag = bag_class.out_tank()
            card.delete_number(bag)
            card.fill_cart()
            text_card = '\n'
            text_card += f'----------Игрок:   {card.num_player}.{card.name}   --------\n'
            assert card.num_player == 1
            assert card.name == 'max'
            y = 0
            assert y == 0
            x = 0
            assert x == 0
            for i in range(3):
                for number in card.len_line:
                    assert card.len_line == range(0, 9)
                    if number in card.list_full_position[i]:
                        assert number in card.list_full_position[i]
                        assert len(card.list_full_position) == 3
                        assert len(card.list_full_position[i]) == 5
                        if card.numbers[y] == None:
                            x += 1
                            assert text_card + f'--  '
                            if x >= 15:
                                assert card.victory == True
                            assert x <= 15
                            y += 1
                        elif card.numbers[y] > 9:
                            assert text_card + f'{card.numbers[y]}  '
                            y += 1
                        else:
                            assert text_card + f' {card.numbers[y]}  '
                            y += 1
                    else:
                        assert not number in card.list_full_position[i]
                        assert text_card + '    '
                assert text_card + '\n'
                assert text_card + ('-' * 35)


class TestPlayer():
    def test__init__(self):
        player = Player(1, 'max', 1)
        player.card = Card(1, 'max')

        assert player.name == 'max'
        assert player.num_player == 1
        assert player.type_player == 1
        assert player.card == player.card
        assert player.decision == None

    def test_action_player(self):

        player = Player(num_player=1, name='max', type_player=1)
        bag_test = Bag()
        player.card = Card(num_player=1, name='max')
        for i in range(90):
            bag = bag_test.out_tank()
            player.card.delete_number(bag)
            requests = ['u', 'n']
            for request in requests:
                player.action_player(bag, request)
                if player.card.is_there_barrel:
                    assert player.card.is_there_barrel == (True)
                    if request == 'u':
                        assert request == 'u'
                        assert player.decision == (False, f'Бачонок №  {bag} из карты  {player.card.num_player}.{player.card.name}   Удален !')
                    else:
                        assert request != 'u'
                        assert player.decision == (True, f'Вы   {player.card.num_player}.{player.card.name}   проиграли ! Бачонок №  {bag} в вашей карте есть !')
                else:
                    assert player.card.is_there_barrel == (False)
                    if request == 'n':
                        assert request == 'n'
                        assert player.decision == (False, f'Все верно! Бачонка №  {bag}  в вашей  карте   {player.card.num_player}.{player.card.name}    нет !')
                    else:
                        assert request != 'n'
                        assert player.decision == (True, f'Не правильный  выбор ! Вы    {player.card.num_player}.{player.card.name}    проиграли !')


class TestRobot():


    def test_action_player(self):
        player = Robot(num_player=1, name='max', type_player=1)
        bag_test = Bag()
        player.card = Card(num_player=1, name='max')
        for i in range(90):
            bag = bag_test.out_tank()
            player.card.delete_number(bag)
            player.action_player(bag, request=None)
            if player.card.is_there_barrel:
                assert player.card.is_there_barrel == (True)
                assert player.decision == (False, f'Бачонок №  {bag} из карты компа  {player.num_player}.{player.name}   Удален !')
            else:
                assert player.card.is_there_barrel == (False)
                assert not bag in player.card.numbers
                assert bag in range(1, 91)
                assert player.decision == (False, f'Бачонка №  {bag}  в  карте компа   {player.num_player}.{player.name}    нет')



# =================================================================== 8 passed in 0.36s ===================================================================
#
# C:\Users\User\PycharmProjects\lesson_10>pytest --cov
# ================================================================== test session starts ==================================================================
# platform win32 -- Python 3.7.4, pytest-5.3.1, py-1.8.0, pluggy-0.13.1
# rootdir: C:\Users\User\PycharmProjects\lesson_10
# plugins: cov-2.8.1
# collected 8 items
#
# test_classis.py ........                                                                                                                           [100%]
#
# ----------- coverage: platform win32, python 3.7.4-final-0 -----------
# Name              Stmts   Miss  Cover
# -------------------------------------
# classis.py           80      0   100%
# test_classis.py     145      0   100%
# -------------------------------------
# TOTAL               225      0   100%
#
#
# =================================================================== 8 passed in 0.38s ===================================================================
#
# C:\Users\User\PycharmProjects\lesson_10>



