from .char import SorcererCharacter
from ..equipment import (
    Item,
    CURSED_RING,
    LEATHER_ARMOR,
    IMBUED_STAFF,
    RING_OF_POLYMORPH,
    ORB,
    DAGGER,
    CROSSBOW,
    SPELLGEM_SPHERE,
    SHATTERGEM,
)
from ..inventory import Wealth, Inventory
from ..spells import (
    Spell,
    FireBolt,
    Fireball,
)

WEALTH = Wealth(
    copper=6,
    silver=0,
    gold=530,
)
WEALTH.dcurrency(
    valg=+5500-100-1-1-150,
    vals=-3-2-6-7-4-2-7-8,
    valc=-5-7-7-3,
)

INVENTORY = Inventory(
    wealth=WEALTH,
    rations=11,
    horse_rations=7,
    torches=10,
    pitons=10,
    various=[
        'Bedroll',
        'Rope, 50ft',
        'Small knife',
        'Crowbar',
        'Hammer',
        'Tinderbox',
        'Waterskin',
        'Quill',
        'Ink',
        'Letter from a dead colleague posing a question you have not yet been able to answer',
    ]
)

EQUIPMENT: dict[str, Item] = {
    CURSED_RING.name: CURSED_RING,
    LEATHER_ARMOR.name: LEATHER_ARMOR,
    IMBUED_STAFF.name: IMBUED_STAFF,
    RING_OF_POLYMORPH.name: RING_OF_POLYMORPH,
    ORB.name: ORB,
    DAGGER.name: DAGGER,
    CROSSBOW.name: CROSSBOW,
    SPELLGEM_SPHERE.name: SPELLGEM_SPHERE,
    SHATTERGEM.name: SHATTERGEM,
}
SPELLS: dict[str, Spell] = {
    FireBolt.name: FireBolt,
    Fireball.name: Fireball,
}


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
    inventory=INVENTORY,
    spells=SPELLS,
)
