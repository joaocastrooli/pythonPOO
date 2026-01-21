from models.Character import Character
from models.Weapon import Weapon

personagemFrix = Character("Cavaleiro", 600, 40)
personagemJoao = Character("Valquiria", 800, 650)
personagemJoao.attack(personagemFrix)
fireball = Weapon("FireBall", 30)
personagemJoao.equipWeapon(fireball)
personagemJoao.attack(personagemFrix)
