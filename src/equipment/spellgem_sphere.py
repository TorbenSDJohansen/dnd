from .equipment import Item


_DESC = '''
This gem-encrusted metal sphere hums with arcane potential. Embedded within its surface are three distinct spell gems, each capable of holding magical energy. The sphere can store up to one 4th-level spell and two 3rd-level spells, which must be cast into their respective gems beforehand. When charged, the gems glow faintly with arcane light.

A creature holding the Spellgem Sphere can cast any stored spell as an action, using the spellcasting ability and save DC of the original caster. If the spell requires concentration, the user of the sphere must maintain it. Once a spell is expended from a gem, that gem becomes inert and cannot be refilled until the next dawn.

To store a spell, a caster must touch the sphere while casting a spell of the appropriate level. The spell is absorbed into an empty gem, disappearing from the caster’s mind as if cast normally. The sphere cannot hold more than one 4th-level spell and two 3rd-level spells at a time.
'''

SPELLGEM_SPHERE = Item(
    name='Spellgem Sphere',
    desc=_DESC,
)
