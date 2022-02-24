class User:
    def __init__(self, userID, ecoStats, battleStats):
        self.userID = userID
        self.ecoStats = ecoStats
        self.battleStats = battleStats

class EcoStats:
    def __init__(self, balance, workMoney, promoBonus, timeRequiredPromo, timeUntilPromo):
            self.balance = balance
            self.workMoney = workMoney
            self.promoBonus = promoBonus
            self.timeRequiredPromo = timeRequiredPromo
            self.timeUntilPromo = timeUntilPromo
    def work(self):
            self.balance += self.workMoney
            self.timeUntilPromo += 1
            if (self.timeRequiredPromo <= self.timeUntilPromo):
                self.workMoney += self.promoBonus
                return True
            return False

class BattleStats:
    def __init__(self, maxHP, HP, maxMana, Mana, inv):
        self.maxHP = maxHP
        self.HP = HP
        self.maxMana = maxMana
        self.Mana = Mana
        self.inv = inv



