class armor():
    def __init__(self, strength, effect, desc):
        self.strength = strength
        self.effect = effect
        self.desc = desc

class primary():
    def __init__(self, damage, effect, desc):
        self.damage = damage
        self.effect = effect
        self.desc = desc

class secondary():
    def __init__(self, effect, desc):
        self.effect = effect
        self.desc = desc

#Armor
iron_armor = armor(5, "Nothing", "Normal iron armor. Nothing special to say about that.")
leather_cap = armor(1, "Nothing", "A nice cozy winter cap to keep you warm during the winter months.")

#Primary
stone_sword = primary(3, "Nothing", "A normal stone sword, common for the warrior class.")

#Secondary
wooden_shield = secondary("Protection 3", "Protects yourself from weak attacks.")
explosives = secondary("Blows Up", "This is pretty self explanitory. Don't play with matches, kids!")        