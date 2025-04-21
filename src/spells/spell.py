from dataclasses import dataclass
from typing import Literal


CastingTime = Literal['A', 'BA', '']
Range = Literal['T'] | int
Component = Literal['V', 'S', 'M'] | str
Shape = Literal['circle', 'cone', 'line']
Damage = tuple[int, int]
DamageType = Literal['fire', 'lightning']


@dataclass
class Spell:
    name: str
    level: int
    cast_range: Range
    components: list[Component]
    casting_time: CastingTime = 'A'
    duration: int = 0

    shape: Shape | None = None
    damage: Damage | list[Damage] | None = None
    damage_type: DamageType | None = None
