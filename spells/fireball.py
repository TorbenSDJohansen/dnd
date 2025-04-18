from .spell import (
    Spell,
)


Fireball = Spell(
    level=3,
    cast_range=150,
    components=['V', 'S', 'M'],
    damage=(8, 6),
    damage_type='fire',
)
