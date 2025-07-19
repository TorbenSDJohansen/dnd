from dataclasses import dataclass


@dataclass
class Wealth:
    copper: int
    silver: int
    gold: int

    def dgold(self, val: int):
        if val < -self.gold:
            raise ValueError('Broke')

        self.gold += val

    def dsilver(self, val: int):
        self.silver += val

        dgold = self.silver // 10

        self.dgold(dgold)
        self.silver -= 10 * dgold

    def dcopper(self, val: int):
        self.copper += val

        dsilver = self.copper // 10

        self.dsilver(dsilver)
        self.copper -= 10 * dsilver

    def dcurrency(self, valg: int = 0, vals: int = 0, valc: int = 0):
        self.dgold(valg)
        self.dsilver(vals)
        self.dcopper(valc)
