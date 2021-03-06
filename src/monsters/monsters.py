from ..skills import skills
from .monster import Monster


class Goldfish(Monster):
    """A pathetic adversary"""

    level = 1
    hp = 15
    max_hp = 15
    energy = 0
    max_energy = 0
    strength = 2
    intelligence = 0
    stamina = 0
    dexterity = 0
    charisma = 0

    skills = [skills["bubble"]]


class Rat(Monster):
    """Disgustic vermin"""

    level = 1
    hp = 25
    max_hp = 25
    energy = 0
    max_energy = 0
    strength = 4
    intelligence = 0
    stamina = 0
    dexterity = 0
    charisma = 0

    skills = [skills["bite"]]


class Quokka(Monster):
    """A smiley rat"""

    level = 1
    hp = 35
    max_hp = 35
    energy = 0
    max_energy = 0
    strength = 5
    intelligence = 0
    stamina = 0
    dexterity = 0
    charisma = 0

    skills = [skills["bite"]]


class Bandit(Monster):
    """A mischevious so-and-so"""

    level = 2
    hp = 40
    max_hp = 40
    energy = 0
    max_energy = 0
    strength = 6
    intelligence = 0
    stamina = 0
    dexterity = 0
    charisma = 0
    gold = 20

    skills = [skills["strike"]]


class Goblin(Monster):
    """A disgusting and cheeky creature"""

    level = 2
    hp = 50
    max_hp = 50
    energy = 0
    max_energy = 0
    strength = 8
    intelligence = 0
    stamina = 0
    dexterity = 0
    charisma = 0
    gold = 10

    skills = [skills["bite"], skills["strike"]]


class Slime(Monster):
    """An inexplicably sentient mass of slime"""

    level = 2
    hp = 60
    max_hp = 60
    energy = 0
    max_energy = 0
    strength = 1
    intelligence = 0
    stamina = 0
    dexterity = 0
    charisma = 0

    skills = [skills["bubble"]]


class Hobgoblin(Monster):
    """An even more disgusting and cheeky creature"""

    level = 3
    hp = 60
    max_hp = 60
    energy = 0
    max_energy = 0
    strength = 12
    intelligence = 2
    stamina = 2
    dexterity = 0
    charisma = 0
    gold = 30

    skills = [skills["bite"], skills["strike"]]
