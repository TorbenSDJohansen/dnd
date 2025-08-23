from dataclasses import dataclass
from typing import Literal

from ..equipment import Item
from ..spells import Spell
from ..inventory import Inventory


Race = Literal[
    "Human",
    "Elf",
    "Dwarf",
    "Halfling",
    "Dragonborn",
    "Gnome",
    "Half-Elf",
    "Half-Orc",
    "Tiefling",
]
Class = Literal[
    "Barbarian",
    "Bard",
    "Cleric",
    "Druid",
    "Fighter",
    "Monk",
    "Paladin",
    "Ranger",
    "Rogue",
    "Sorcerer",
    "Warlock",
    "Wizard",
]
Background = Literal[
    "Acolyte",
    "Charlatan",
    "Criminal",
    "Entertainer",
    "Folk Hero",
    "Guild Artisan",
    "Hermit",
    "Noble",
    "Outlander",
    "Sage",
    "Sailor",
    "Soldier",
    "Urchin",
]
Skill = Literal[
    "acrobatics",
    "animal_handling",
    "arcana",
    "athletics",
    "deception",
    "history",
    "insight",
    "intimidation",
    "investigation",
    "medicine",
    "nature",
    "perception",
    "performance",
    "persuasion",
    "religion",
    "sleight_of_hand",
    "stealth",
    "survival",
]
Attribute = Literal[
    "strength",
    "dexterity",
    "constitution",
    "intelligence",
    "wisdom",
    "charisma",
]


@dataclass
class Character:
    name: str
    race: Race
    cclass: Class
    level: int
    background: str
    armor_class: int
    initiative: int
    speed: int
    inspiration: bool

    # Attributes
    strength: int
    dexterity: int
    constitution: int
    intelligence: int
    wisdom: int
    charisma: int

    # Hit Points
    hp_max: int

    # Proficiencies
    proficiency_bonus: int
    proficiencies: list[Skill | Attribute]

    # Complex
    inventory: Inventory
    spells: list[Spell] = None
    equipment: dict[str, Item] = None

    # Skills
    def skill_bonus(self, skill: Skill) -> int:
        skill_to_attribute = {
            "acrobatics": self.dexterity,
            "animal_handling": self.wisdom,
            "arcana": self.intelligence,
            "athletics": self.strength,
            "deception": self.charisma,
            "history": self.intelligence,
            "insight": self.wisdom,
            "intimidation": self.charisma,
            "investigation": self.intelligence,
            "medicine": self.wisdom,
            "nature": self.intelligence,
            "perception": self.wisdom,
            "performance": self.charisma,
            "persuasion": self.charisma,
            "religion": self.intelligence,
            "sleight_of_hand": self.dexterity,
            "stealth": self.dexterity,
            "survival": self.wisdom,
        }

        bonus = (skill_to_attribute[skill] - 10) // 2

        if skill in self.proficiencies:
            bonus += self.proficiency_bonus

        return bonus

    def saving_throw_bonus(self, attribute: Attribute) -> int:
        attribute_to_value = {
            "strength": self.strength,
            "dexterity": self.dexterity,
            "constitution": self.constitution,
            "intelligence": self.intelligence,
            "wisdom": self.wisdom,
            "charisma": self.charisma,
        }

        bonus = (attribute_to_value[attribute] - 10) // 2

        if attribute in self.proficiencies:
            bonus += self.proficiency_bonus

        return bonus


class SorcererCharacter(Character):
    spell_slot_table = {
        1: [2],
        2: [3],
        3: [4, 2],
        4: [4, 3],
        5: [4, 3, 2],
        6: [4, 3, 3],
        7: [4, 3, 3, 1],
        8: [4, 3, 3, 2],
        9: [4, 3, 3, 3, 1],
        10: [4, 3, 3, 3, 2],
        11: [4, 3, 3, 3, 2, 1],
        12: [4, 3, 3, 3, 2, 1],
        13: [4, 3, 3, 3, 2, 1, 1],
        14: [4, 3, 3, 3, 2, 1, 1],
        15: [4, 3, 3, 3, 2, 1, 1, 1],
        16: [4, 3, 3, 3, 2, 1, 1, 1],
        17: [4, 3, 3, 3, 2, 1, 1, 1, 1],
        18: [4, 3, 3, 3, 3, 1, 1, 1, 1],
        19: [4, 3, 3, 3, 3, 2, 1, 1, 1],
        20: [4, 3, 3, 3, 3, 2, 2, 1, 1],
    }
    spell_slot_sp_cost = {1: 2, 2: 3, 3: 5, 4: 6, 5: 7}

    @property
    def sorcery_points(self) -> int:
        if self.level < 2:
            return 0

        return self.level

    @property
    def spell_attack_bonus(self) -> int:
        bonus = (self.charisma - 10) // 2 + self.proficiency_bonus
        bonus += sum(item.dspell_attack for item in self.equipment.values())

        return bonus

    @property
    def spell_save_dc(self) -> int:
        dc = 8 + (self.charisma - 10) // 2 + self.proficiency_bonus
        dc += sum(item.dspell_save_dc for item in self.equipment.values())

        return dc

    @property
    def num_attuned_items(self) -> int:
        return sum(1 for item in self.equipment.values() if item.attuned)

    def spell_slots(self, spell_level: int) -> int:
        slots = self.spell_slot_table[self.level]

        return slots[spell_level - 1] if spell_level <= len(slots) else 0

    def sorcery_point_cost(self, spell_level: int) -> int:
        return self.spell_slot_sp_cost[spell_level]
