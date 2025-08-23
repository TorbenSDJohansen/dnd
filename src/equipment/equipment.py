from dataclasses import dataclass


@dataclass
class Item:
    name: str
    desc: str
    attuned: bool | None = None

    # AC
    ac: int | None = None
    dac: int = 0

    # Damage
    ddamage: int = 0
    ddamage_fire: int = 0

    # Spell attack and save DC
    dspell_attack: int = 0
    dspell_save_dc: int = 0
