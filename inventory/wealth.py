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

    def dcurrency(self, valg: int, vals: int, valc: int):
        self.dgold(valg)
        self.dsilver(vals)
        self.dcopper(valc)


WEALTH = Wealth(
    copper=6,
    silver=0,
    gold=530,
)

WEALTH.dcurrency(
    valg=+5500-100-1-1-150,
    vals=-3-2-6-7-4-2-7-8,
    valc=-5-7-7-3,
)

print(WEALTH)
