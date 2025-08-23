from .equipment import Item


EMBERWELL_VIAL = Item(
    name='Emberwell Vial',
    desc='Inner Fire Recovery: When rolling Hit Dice to recover hit points, regain 1 sorcery point per 3 Hit Dice rolled. Once per dawn.',
    attuned=True,
    dspell_attack=1,
    dspell_save_dc=1
)
