from dataclasses import dataclass

from .wealth import Wealth, WEALTH


@dataclass
class Inventory:
    wealth: Wealth
    rations: int
    horse_rations: int
    torches: int
    pitons: int
    various: list[str]


INVENTORY = Inventory(
    wealth=WEALTH,
    rations=11,
    horse_rations=7,
    torches=10,
    pitons=10,
    various=[
        'Bedroll',
        'Rope, 50ft',
        'Small knife',
        'Crowbar',
        'Hammer',
        'Tinderbox',
        'Waterskin',
        'Quill',
        'Ink',
        'Letter from a dead colleague posing a question you have not yet been able to answer',
    ]
)
