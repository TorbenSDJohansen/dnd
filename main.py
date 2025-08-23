import random

from src.chars import VALGROTG_EMBERSTONE


def cast_damage_spell(name: str):
    spell = VALGROTG_EMBERSTONE.spells[name]
    damage = 0

    num_dice, die = spell.damage

    for _ in range(num_dice):
        hit = random.randint(1, die)

        if spell.damage_type == 'fire' and hit == 1:
            hit = 2

        damage += hit

    ddamage = sum(item.ddamage for item in VALGROTG_EMBERSTONE.equipment.values())
    damage += ddamage

    if spell.damage_type == 'fire':
        ddamage_fire = sum(item.ddamage_fire for item in VALGROTG_EMBERSTONE.equipment.values())
        damage += ddamage_fire

    return damage


def main():
    for key, value in VALGROTG_EMBERSTONE.inventory.__dict__.items():
        print(key, value)

    for name, item in VALGROTG_EMBERSTONE.equipment.items():
        print(name, item)

    damages = []

    for _ in range(1000):
        damages.append(cast_damage_spell('Fire Bolt'))

    print(min(damages), max(damages), sum(damages) / len(damages))

    damages = []

    for _ in range(100000):
        damages.append(cast_damage_spell('Fireball'))

    print(min(damages), max(damages), sum(damages) / len(damages))

    # from matplotlib import pyplot as plt
    # plt.hist(damages, bins=100)
    # plt.show()

    print(VALGROTG_EMBERSTONE.spell_slots(1))
    print(VALGROTG_EMBERSTONE.spell_slots(2))
    print(VALGROTG_EMBERSTONE.spell_slots(3))
    print(VALGROTG_EMBERSTONE.spell_slots(4))

    print(VALGROTG_EMBERSTONE.spell_attack_bonus)
    print(VALGROTG_EMBERSTONE.spell_save_dc)
    print(VALGROTG_EMBERSTONE.num_attuned_items)


if __name__ == '__main__':
    main()
