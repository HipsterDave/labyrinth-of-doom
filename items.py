class armor():
    def __init__(self, name, strength, effect, desc):
        self.name = name
        self.strength = strength
        self.effect = effect
        self.desc = desc

class primary():
    def __init__(self, name, damage, effect, desc):
        self.name = name
        self.damage = damage
        self.effect = effect
        self.desc = desc

class secondary():
    def __init__(self, name, effect, desc):
        self.name = name
        self.effect = effect
        self.desc = desc

#Armor
no_armor = armor("Nothing", 0, "Nothing", "Nothing")
iron_armor = armor("Iron Armor", 5, "Nothing", "Normal iron armor. Nothing special to say about that.")
leather_cap = armor("Leather Cap", 1, "Nothing", "A nice cozy winter cap to keep you warm during the winter months.")

#Primary
no_primary = primary("Nothing", 0, "Nothing", "Nothing")
stone_sword = primary("Stone Sword", 1, "Nothing", "A normal stone sword, common for the warrior class.")

#Secondary
no_secondary = secondary("Nothing", "Nothing", "Nothing")
wooden_shield = secondary("Wooden Shield", "Protection 3", "Protects yourself from weak attacks.")
explosives = secondary("Explosives", "Blows Up", "This is pretty self explanitory. Don't play with matches, kids!")   