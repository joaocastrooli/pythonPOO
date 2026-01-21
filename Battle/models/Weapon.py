class Weapon:
    def __init__(self, weapon, damageBonus):
        self.__weapon = weapon
        self.__damageBonus = damageBonus

    @property
    def weapon(self):
        return self.__weapon
    
    @property
    def damageBonus(self):
        return self.__damageBonus