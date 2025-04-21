import random

from src.inventory import INVENTORY
from src.spells import SPELLS
from src.equipment import EQUIPMENT
from src.chars import VALGROTG_EMBERSTONE


def cast_damage_spell(name: str):
    spell = SPELLS[name]
    damage = 0

    num_dice, die = spell.damage

    for _ in range(num_dice):
        hit = random.randint(1, die)

        if spell.damage_type == 'fire' and hit == 1:
            hit = 2

        damage += hit

    ddamage = sum(item.ddamage for item in EQUIPMENT.values())
    damage += ddamage

    if spell.damage_type == 'fire':
        ddamage_fire = sum(item.ddamage_fire for item in EQUIPMENT.values())
        damage += ddamage_fire

    return damage


def main():
    # for key, value in INVENTORY.__dict__.items():
    #     print(key, value)

    # for name, item in EQUIPMENT.items():
    #     print(name, item)

    # damages = []

    # for _ in range(1000):
    #     damages.append(cast_damage_spell('Fire Bolt'))

    # print(damages)

    # damages = []

    # for _ in range(100000):
    #     damages.append(cast_damage_spell('Fireball'))

    # print(damages)

    # from matplotlib import pyplot as plt
    # plt.hist(damages, bins=100)
    # plt.show()

    print(VALGROTG_EMBERSTONE.spell_slots(1))
    print(VALGROTG_EMBERSTONE.spell_slots(2))
    print(VALGROTG_EMBERSTONE.spell_slots(3))
    print(VALGROTG_EMBERSTONE.spell_slots(4))




if __name__ == '__main__':
    main()
