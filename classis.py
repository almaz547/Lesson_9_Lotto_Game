import random

class Bag:
    def __init__(self):
        self.game_bag = list(range(1, 91))

    def out_tank(self):                                               # Достать один бачонок
        if self.game_bag:
            tank = random.sample(self.game_bag, 1)
            for el in tank:
                tank = el
            self.game_bag.remove(tank)
            return tank
        else:
            return print('Пешочек пуст')



class Card():
    def __init__(self, name):
        self.count_number = range(1, 91)                            # Общий ряд чисел
        self.len_line = range(9)                              # Количество позиций в линии
        self.list_full_position = []                         # Список списков номеров позиций для заполнения
        self.name = name
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
            return True
        else:
            return False



    def fill_cart(self):                            # Заполняем карточку
        y = 0                                            # Определяем порядковый индекс для  15-ти цифр в карточке
        x = 0                                       # Счетчик зачеркнутых номеров
        print(f'----------Игрок:   {self.name[0]}.{self.name[1]}   --------')
        for i in range(3):
            for number in self.len_line:                               # Проходим по 9 позициям в линии
                if number in self.list_full_position[i]:                # Если позиция совпадает с номером для записи
                    if self.numbers[y] == None:
                        x += 1
                        print('--  ', end='')
                        if x >= 15:
                            print(f'Карточка {self.name[1]} пуста')
                            print(f'Победа   {self.name[1]}  ! ! !')

                        y += 1
                    elif self.numbers[y] > 9:
                        print(f'{self.numbers[y]}  ', end='')              # Записываем в нее цифру по индексу
                        y += 1                                      # Переключаем счетчик индекса 15-ти цифр карточки
                    else:
                        print(f' {self.numbers[y]}  ', end='')
                        y += 1
                else:
                    print('    ', end='')                      # На остальных четырех пустых позициях печатаем пробел
            print('')
        print('-' * 35)


'''
Следующий вариант думаю будет прогрессивнее, с большим количеством использования классов.
'''




