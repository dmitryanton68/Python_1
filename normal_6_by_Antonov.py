# Задача - 1
# Ранее мы с вами уже писали игру, используя словари в качестве
# структур данных для нашего игрока и врага, давайте сделаем новую, но уже с ООП
# Опишите базовый класс Person, подумайте какие общие данные есть и у врага и у игрока
# Не забудьте, что у них есть помимо общих аттрибутов и общие методы.
# Теперь наследуясь от Person создайте 2 класса Player, Enemy.
# У каждой сущности должы быть аттрибуты health, damage, armor
# У каждой сущности должно быть 2 метода, один для подсчета урона, с учетом брони противника,
# второй для атаки противника.
# Функция подсчета урона должна быть инкапсулирована
# Вам надо описать игровой цикл так же через класс.
# Создайте экземпляры классов, проведите бой. Кто будет атаковать первым оставляю на ваше усмотрение.

class Person:
    def __init__(self, health, armor):
        self.health = health
        self.armor = armor
        self.attack_power = 0.3 * self.health
        self.damage = 0.5 * self.attack_power - 0.1 * self.armor

    @property
    def attack(self):
        print(f'attack_power = {self.attack_power}')
        return self.attack_power

    @property
    def score_damage(self):

        if self.armor > 0 and self.attack_power > 0:
            self.damage = self.damage
            self.armor = self.armor * 0.8
        elif self.armor <= 0 and self.attack_power > 0:
            self.damage = 0.5 * self.attack_power
        elif self.armor <= 0 and self.attack_power <= 0:
            self.damage = 0
        return self.damage


class Player(Person):
    def __init__(self, health, armor):
        Person.__init__(self, health, armor)


class Enemy(Person):
    def __init__(self, health, armor):
        Person.__init__(self, health, armor)


class Game:
    def __init__(self, first_player, second_player, steps=1):
        self.first_player = first_player
        self.second_player = second_player
        self.steps = steps

    @property
    def cycle(self):
        i = 1
        while i <= self.steps:
            if i % 2 != 0:
                self.second_player.health = self.second_player.health - self.second_player.score_damage
                if self.second_player.health > self.second_player.damage:
                    self.second_player.health = self.second_player.health - self.second_player.damage
                    print(
                        f'-Step {i}. {self.first_player.__class__.__name__} health = {self.first_player.health}, {self.second_player.__class__.__name__} health = {self.second_player.health}')
                else:
                    self.second_player.health = 0
                    return f'Step {i}. Game over: {self.second_player.__class__.__name__} health = {self.second_player.health}, {self.first_player.__class__.__name__} win - {self.second_player.__class__.__name__} is dead'
                i += 1
            else:
                self.first_player, self.second_player = self.second_player, self.first_player
                self.second_player.health = self.second_player.health - self.second_player.score_damage
                if self.second_player.health > self.second_player.damage:
                    self.second_player.health = self.second_player.health - self.second_player.damage
                    print(
                        f'+Step {i}. {self.first_player.__class__.__name__} health = {self.first_player.health}, {self.second_player.__class__.__name__} health = {self.second_player.health}')
                else:
                    self.second_player.health = 0
                    return f'Step {i}. Game over: {self.second_player.__class__.__name__} health = {self.second_player.health}, {self.first_player.__class__.__name__} win - {self.second_player.__class__.__name__} is dead'
                i += 1


a = Player(100, 100)
b = Enemy(100, 100)
print(Game(a, b, 22).cycle)
