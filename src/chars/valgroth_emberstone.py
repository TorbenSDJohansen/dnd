from .char import SorcererCharacter
from ..equipment import EQUIPMENT
from ..inventory import INVENTORY


VALGROTG_EMBERSTONE = SorcererCharacter(
    name="Valgroth",
    race="Dwarf",
    cclass="Sorcerer",
    level=7,
    background="Sage",
    armor_class=5,
    initiative=-1,
    speed=25,
    inspiration=True,
    strength=10,
    dexterity=9,
    constitution=12,
    intelligence=12,
    wisdom=12,
    charisma=12,
    hp_max=38,
    proficiency_bonus=3,
    proficiencies=["arcana", "history", "insight", "constitution", "charisma"],
    equipment=EQUIPMENT,
    inventory=INVENTORY
)
