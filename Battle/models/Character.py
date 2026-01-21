class Character:
    def __init__(self, name, life, strength):
        self.__name = name
        self.__life = life
        self.__strength = strength
        self.__weapon = None

    def attack(self, opponent):
        print(f"{self.__name} ataca {opponent.name}")
        if self.__weapon == None:
            opponent.receiveDamage(self.__strength)
        else: 
            opponent.receiveDamage(self.__strength + self.__weapon.damageBonus)
    
    def receiveDamage(self, strength):
        if strength > self.__life:
            print(f"{self.name} morreu")
        else:
            self.__life -= strength
            print(f"{self.name} recebeu um ataque de {strength} de dano. Sua vida agora é {self.__life}")

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        if len(value) > 3:
            self.__name = value
        else: raise ValueError("Menor que 3 Caracteres")
    
    def __str__(self):
        return f"Personagem [{self.__name}] - HP: [{self.__life}] - Força: [{self.__strength}]"
    
    def equipWeapon(self, weapon):
        self.__weapon = weapon

