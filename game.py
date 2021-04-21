from random import random, randint, choice, choices


class Player:
    """Класс Игрока

    """

    def __init__(self, name):
        self.name = name  # имя игрока
        self.hp = 100  # здоровье игрока
        self.low_hit = randint(18, 25)  # урон в небольшом диапазоне
        self.high_hit = randint(10, 35)  # урон в большом диапазоне
        self.heal = randint(18, 25)  # лечение в небольшом диапазоне
        self.act = [self.do_low_hit, self.do_high_hit, self.do_heal]  # массив действий для игрока

    def do_low_hit(self, enemy):
        """Функция для нанесения умеренного урона с небольшим диапозоном 

        """
        print(f'\n*** {self.name}, Ваш урон в небольшом диапазоне (18-25) равен: {self.low_hit}dmg\n')

        enemy.hp -= self.low_hit
        if enemy.hp < 0:  # нижняя граница жизней
            enemy.hp = 0
        print(f'--> {self.name} ранил {enemy.name}a на {self.low_hit} единиц урона!')

        print(f'\n*** {enemy.name} HP(♥): {enemy.hp}hp')
        print(f'*** {self.name} HP(♥): {self.hp}hp')

    def do_high_hit(self, enemy):
        """Функция для нанесения урона с большим диапозоном

        """
        print(f'\n*** {self.name}, Ваш урон в большом диапазоне (10-35) равен: {self.high_hit}dmg\n')

        enemy.hp -= self.high_hit
        if enemy.hp < 0:  # нижняя граница жизней
            enemy.hp = 0
        print(f'--> {self.name} ранил {enemy.name}a на {self.high_hit} единиц урона!')

        print(f'\n*** {enemy.name} HP(♥): {enemy.hp}hp')
        print(f'*** {self.name} HP(♥): {self.hp}hp')

    def do_heal(self):
        """Функция для исцеления в небольшом диапазоне

        """
        print(f'\n*** {self.name} решил исцелить себя на +{self.heal}hp!')
        print(f'*** {self.name}, на данный момент Ваше здоровье: {self.hp}hp')

        self.hp += self.heal
        if self.hp > 100:  # верхняя граница полных жизней
            self.hp = 100
        print(f'\n--> {self.name} исцелил себя на {self.heal}hp!')

        print(f'\n*** {self.name} HP(♥): {self.hp}hp')
        return self.hp

    def do_act(self, enemy):
        """Функция для выбора атаки

        """
        random_choice = choice(self.act)  # рандомный выбор атаки
        if random_choice != self.do_heal:
            random_choice = random_choice(enemy)
            return random_choice
        else:
            return random_choice()


class Computer(Player):
    """Класс Компьютера, наследует класс Игрока

    """

    def do_act(self, enemy):
        """Функция для выбора атаки

        """
        random_choice = choice(self.act)  # рандомный выбор атаки
        if self.hp < 35:
            random_choice = choices(self.act, [15, 15, 70], k=1)[0]  # рандом, с большей вероятностью излечения

        if random_choice != self.do_heal:
            random_choice = random_choice(enemy)
            return random_choice
        else:
            return random_choice()


def new_game(first_player, second_player):
    """Функция алгоритма работы игры

    """
    count_act = 1
    print('\n' + '*' * 72)
    print(f'{" " * 26}*** START GAME! ***')
    print('*' * 72 +'\n')
    print(f'*** ИГРОК №1: {first_player.name}')
    print(f'*** ИГРОК №2: {second_player.name}\n')

    while first_player.hp > 0 and second_player.hp > 0:
        random_turn = random()  # рандомное число для определения игрока, который будет делать ход
        print('-' * 72)
        print(f'|{" " * 30}- ХОД №{count_act} - ')
        print('-' * 72)

        if random_turn > 0.5:
            print(f'\n*** Сейчас ход {first_player.name}a!'.upper())
            first_player.do_act(second_player)
        else:
            print(f'\n*** Сейчас ход {second_player.name}a!'.upper())
            second_player.do_act(first_player)

        print('-' * 72 + '\n')
        count_act += 1
    else:
        if first_player.hp <= 0:
            print(f'\n† † †  {first_player.name} DEAD! † † † \n\n░░░░░ '
                  f'{second_player.name} WIN! CONGRATULATIONS!!! ░░░░░'.upper())
        elif second_player.hp <= 0:
            print(f'\n† † †  {second_player.name} DEAD! † † † \n\n░░░░░ '
                  f'{first_player.name} WIN! CONGRATULATIONS!!! ░░░░░'.upper())
        print('\n' + '*' * 72)
        print(f'{" " * 26}*** GAME OVER! ***')
        print('*' * 72)


computer = Computer("ComputerBot")  # инстанс класса
human = Player("HumanBot")  # инстанс класса

new_game(computer, human)  # вызов функции новой игры
