class Hero:
    username: str
    health: float
    damage: float
    level: int

    def __init__(self, username: str, level: int, health: float, damage: float):
        self.username = username
        self.level = level
        self.health = health
        self.damage = damage

    def battle(self, enemy_hero):
        if enemy_hero.username == self.username:
            raise Exception("You cannot fight yourself")

        if self.health <= 0:
            raise ValueError("Your health is lower than or equal to 0. You need to rest")

        if enemy_hero.health <= 0:
            raise ValueError(f"You cannot fight {enemy_hero.username}. He needs to rest")

        player_damage = self.damage * self.level
        enemy_hero_damage = enemy_hero.damage * enemy_hero.level

        self.health -= enemy_hero_damage
        enemy_hero.health -= player_damage

        if self.health <= 0 and enemy_hero.health <= 0:
            return "Draw"

        if enemy_hero.health <= 0:
            self.level += 1
            self.health += 5
            self.damage += 5
            return "You win"

        enemy_hero.level += 1
        enemy_hero.health += 5
        enemy_hero.damage += 5
        return "You lose"

    def __str__(self):
        return f"Hero {self.username}: {self.level} lvl\n" \
               f"Health: {self.health}\n" \
               f"Damage: {self.damage}\n"



from unittest import TestCase, main

class TestHero(TestCase):
    username = "Test Hero"
    level = 5
    health = 16.8
    damage = 9.4

    def setUp(self):
        self.hero = Hero(self.username, self.level, self.health, self.damage)

    def test_init(self):
        self.assertEqual(self.username, self.hero.username)
        self.assertEqual(self.level, self.hero.level)
        self.assertEqual(self.health, self.hero.health)
        self.assertEqual(self.damage, self.hero.damage)

    def test_attribute_types(self):
        self.assertIsInstance(self.hero.username, str)
        self.assertIsInstance(self.hero.level, int)
        self.assertIsInstance(self.hero.health, float)
        self.assertIsInstance(self.hero.damage, float)

    def test_enemy_hero_has_same_name(self):
        enemy = Hero(self.username, self.level, self.health, self.damage)
        with self.assertRaises(Exception) as ex:
            self.hero.battle(enemy)
        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_hero_health_not_enough(self):
        self.hero.health = 0
        enemy = Hero("Enemy", self.level, self.health, self.damage)

        with self.assertRaises(ValueError) as er:
            self.hero.battle(enemy)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(er.exception))

        self.hero.health = -1
        enemy = Hero("Enemy", self.level, self.health, self.damage)

        with self.assertRaises(ValueError) as er_2:
            self.hero.battle(enemy)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(er_2.exception))


    def test_enemy_health_not_enough(self):
        enemy = Hero("Enemy", self.level, 0, self.damage)
        with self.assertRaises(ValueError) as er:
            self.hero.battle(enemy)
        self.assertEqual("You cannot fight Enemy. He needs to rest", str(er.exception))

        enemy = Hero("Enemy", self.level, -1, self.damage)
        with self.assertRaises(ValueError) as er:
            self.hero.battle(enemy)
        self.assertEqual("You cannot fight Enemy. He needs to rest", str(er.exception))

    def test_draw(self):
        enemy = Hero("Enemy", self.level, self.health, self.damage)
        result = self.hero.battle(enemy)

        self.assertEqual("Draw", result)
        self.assertEqual(self.level, self.hero.level)
        self.assertEqual(5, self.hero.level)
        self.assertEqual(self.damage, self.hero.damage)

    def test_hero_wins(self):
        enemy = Hero("Enemy", 1, 1, 1)
        result = self.hero.battle(enemy)

        self.assertEqual(6, self.hero.level)
        self.assertEqual(20.8, self.hero.health)
        self.assertEqual(14.4, self.hero.damage)
        self.assertEqual("You win", result)


    def test_hero_loses(self):
        self.hero.health = 10
        self.hero.damage = 10
        enemy = Hero("Enemy", 100, 100, 100)

        result = self.hero.battle(enemy)
        self.assertEqual(101, enemy.level)
        self.assertEqual(55, enemy.health)
        self.assertEqual(105, enemy.damage)
        self.assertEqual("You lose", result)

    def test_string(self):
        expected = f"Hero {self.username}: {self.level} lvl\n" \
               f"Health: {self.health}\n" \
               f"Damage: {self.damage}\n"
        self.assertEqual(expected, str(self.hero))

if __name__ == "__main__":
    main()
