from .equipment import Item


CURSED_RING = Item(
    name='Cursed Ring',
    desc='+1 DMG on all attacks. -5 AC',
    attuned=True,
    dac=-5,
    ddamage=1,
)
