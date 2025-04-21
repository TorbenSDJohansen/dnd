from .equipment import Item


RING_OF_POLYMORPH = Item(
    name='Ring of Polymorph',
    desc='This ring allows its wearer to adopt the form of another creature for an extended duration, ensuring the transformation aligns perfectly with their intent. Self-Polymorph Only: While wearing this ring, you can cast the polymorph spell on yourself only. The spell cannot target other creatures. Charges: The ring has 1 charge and regains its expended charge daily at dawn. Extended Duration: When you cast polymorph using the ring, the transformation lasts for 24 hours, or until you drop to 0 hit points, whichever comes first. Intent Control: The transformation aligns exactly with your intended form, provided it adheres to the restrictions of the polymorph spell (e.g., CR ≤ your level, beast only). No unintended or random transformations occur.',
    attuned=True,
)
