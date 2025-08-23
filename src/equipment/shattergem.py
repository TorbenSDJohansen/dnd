from .equipment import Item


_DESC = '''
This fist-sized gemstone pulses with latent arcane energy, its core swirling with trapped magic. A 3rd-level spell can be stored within it by a spellcaster, vanishing from their mind as if cast normally.

A creature can throw the Shattergem (range 30 feet) or crush it in their hand as an action, instantly releasing the stored spell. The spell uses the original caster’s spell attack bonus and save DC but does not require concentration. However, its magic is unstable—any spell with a duration longer than instantaneous lasts only until the end of the current combat round before dissipating.

Once shattered, the gem is destroyed, its arcane energy expended.
'''

SHATTERGEM = Item(
    name='Shattergem',
    desc=_DESC,
)
