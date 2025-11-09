from dataclasses import dataclass

from .wealth import Wealth


@dataclass
class Inventory:
    wealth: Wealth
    rations: int
    horse_rations: int
    torches: int
    pitons: int
    crossbow_bolts: int
    greater_healing_potions: int = 0
    healing_potions: int = 0
    various: list[str]
