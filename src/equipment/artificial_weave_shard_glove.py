from .equipment import Item


ARTIFICIAL_WEAVE_SHARD_GLOVE = Item(
    name='Artificial Weave Shard Glove',
    desc='Weave Satiation: As a bonus action, you can take 1d10 necrotic damage that cannot be reduced or avoided to empower your next spell attack. When you hit with that attack within the next hour, it deals an extra 1d20 force damage. Usable once per long rest.',
    attuned=True,
    ddamage=1,
    dspell_attack=1,
)
