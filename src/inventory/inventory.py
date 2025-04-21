from dataclasses import dataclass

from .wealth import Wealth


@dataclass
class Inventory:
    wealth: Wealth
    rations: int
    horse_rations: int
    torches: int
    pitons: int
    various: list[str]
