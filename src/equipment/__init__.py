from .equipment import Item
from .cursed_ring import CURSED_RING
from .leather_armor import LEATHER_ARMOR
from .imbued_staff import IMBUED_STAFF
from .ring_of_polymorph import RING_OF_POLYMORPH
from .orb import ORB
from .dagger import DAGGER
from .crossbow import CROSSBOW
from .spellgem_sphere import SPELLGEM_SPHERE
from .shattergem import SHATTERGEM


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
