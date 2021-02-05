import random

# player
class Player:
    """this contains the player attributes and damage """

    def __init__(self, name, attack, health, defense, buffs):
        self.name = name
        self.attack = attack
        self.health = health
        self.defense = defense
        self.buffs = buffs

    # player damage calc
    def damage(self):
        tot_attack = self.attack * self.buffs
        player_damage = random.randrange(tot_attack / 2, tot_attack + 1)
        return player_damage


# monster
class Monster:
    """ monster related attributes and damage """

    def __init__(self, attack, health, defense):
        self.attack = attack
        self.health = health
        self.defense = defense

    # monster damage calc
    def damage(self):
        normal_monster_damage = self.attack * 1
        return normal_monster_damage
