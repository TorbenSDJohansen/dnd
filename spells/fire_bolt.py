from .spell import (
    Spell,
)


FireBolt = Spell(
    level=0,
    cast_range=120,
    components=['V', 'S'],
    damage=(2, 10),
    damage_type='fire',
)
