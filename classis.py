import random

class Bag:
    def __init__(self):
        self.game_bag = list(range(1, 91))              # Содержимое мешка
        self.numer_motion = 0                           #  Номер хода

    def out_tank(self):                                               # Достать один бачонок
        if self.game_bag:
            self.numer_motion += 1
            tank = random.sample(self.game_bag, 1)
            for el in tank:
                tank = el
            self.game_bag.remove(tank)
            return tank




class Card():
    def __init__(self, num_player, name):
        self.count_number = range(1, 91)                            # Общий ряд чисел
        self.len_line = range(9)                              # Количество позиций в линии
        self.list_full_position = []                         # Список списков номеров позиций для заполнения
        self.name = name
        self.num_player = num_player
        self.is_there_barrel = False        # Есть ли такая бочка в номерах карты
        self.victory = False
                                                                # Выбрать 15 цифр для карточки
        self.numbers = random.sample(range(1, 91), 15)                # Ряд цифр для карточки
        self.numbers.sort()                                           # Ряд цифр для карточки по порядку
                                                               # Выбор номеров позиций в линиях для заполнения цифрами карты
        for i in range(3):
            full_line_position = random.sample(self.len_line, 5)       # Получаем 5 номера позиций для заполнения цифрами линии
            full_line_position.sort()                                  # Номера позиций для заполнения цифрами линии по порядку
            self.list_full_position.append(full_line_position)


    def delete_number(self, bag):                       # Удаляем номер из списка для карточки
        if bag in self.numbers:
            x = self.numbers.index(bag)
            self.numbers.remove(bag)
            self.numbers.insert(x, None)
            self.is_there_barrel = True
        else:
            self.is_there_barrel = False                 # Есть ли такая бочка в номерах карты



    def fill_cart(self):                            # Заполняем карточку
        y = 0                                            # Определяем порядковый индекс для  15-ти цифр в карточке
        x = 0                                       # Счетчик зачеркнутых номеров
        text_card = '\n'
        text_card += f'----------Игрок:   {self.num_player}.{self.name}   --------\n'
        for i in range(3):
            for number in self.len_line:                               # Проходим по 9 позициям в линии
                if number in self.list_full_position[i]:                # Если позиция совпадает с номером для записи
                    if self.numbers[y] == None:
                        x += 1
                        text_card += f'--  '
                        if x >= 15:
                            self.victory = True
                        y += 1
                    elif self.numbers[y] > 9:
                        text_card += f'{self.numbers[y]}  '              # Записываем в нее цифру по индексу
                        y += 1                                      # Переключаем счетчик индекса 15-ти цифр карточки
                    else:
                        text_card += f' {self.numbers[y]}  '
                        y += 1
                else:
                    text_card += '    '                      # На остальных четырех пустых позициях печатаем пробел
            text_card += '\n'
        text_card += ('-' * 35)
        return text_card


class Player():
    def __init__(self, num_player, name, type_player):
        self.name = name
        self.num_player = num_player
        self.type_player = type_player
        self.card = Card(num_player, name)
        self.decision = None


    def action_player(self, bag, request):
        if self.card.is_there_barrel:
            if request == 'u':
                self.decision = False, f'Бачонок №  {bag} из карты  {self.num_player}.{self.name}   Удален !'
            else:
                self.decision = True, f'Вы   {self.num_player}.{self.name}   проиграли ! Бачонок №  {bag} в вашей карте есть !'
        else:
            if request == 'n':
                self.decision = False, f'Все верно! Бачонка №  {bag}  в вашей  карте   {self.num_player}.{self.name}    нет !'
            else:
                self.decision = True, f'Не правильный  выбор ! Вы    {self.num_player}.{self.name}    проиграли !'
        return self.decision

class Robot(Player):

    def action_player(self, bag, request):
        if self.card.is_there_barrel:
            self.decision = False, f'Бачонок №  {bag} из карты компа  {self.num_player}.{self.name}   Удален !'
        else:
            self.decision = False, f'Бачонка №  {bag}  в  карте компа   {self.num_player}.{self.name}    нет'
        return self.decision











