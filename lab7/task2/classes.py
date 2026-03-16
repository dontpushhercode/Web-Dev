class MagicEntity:
    def __init__(self, name, power, health):
        self.name = name
        self.power = power
        self.health = health
    
    def attack(self, other):
        damage = self.power
        other.health -= damage
        print(f"{self.name} attacks {other.name} for {damage} damage!")
    
    def is_alive(self):
        return self.health > 0

    def speak(self):
        print(f"{self.name} says: 'I am a magical entity!'")

    def __str__(self):
        return f"{self.name} (Power: {self.power}, Health: {self.health})"

class Fairy(MagicEntity):
    def __init__(self, name, power, health, magicDust):
        super().__init__(name, power, health)
        self.magicDust = magicDust

    #overriding
    def attack(self, other):
        damage = self.power + self.magicDust
        other.health -= damage
        print(f"{self.name} attacks {other.name} with magic dust for {damage} damage!")

    def heal(self):
        heal_amount = self.magicDust
        self.health += heal_amount
        print(f"{self.name} heals for {heal_amount} health!")
    
    #overriding
    def speak(self):
        print(f"{self.name} says: 'I am fairy! Look at my fabulous wings!'")

    #overriding
    def __str__(self):
        return f"{self.name} the Fairy (Power: {self.power}, Health: {self.health}, Magic Dust: {self.magicDust})"

class Witch(MagicEntity):
    def __init__(self, name, power, health, potionPower):
        super().__init__(name, power, health)
        self.potionPower = potionPower

    #overriding
    def attack(self, other):
        damage = self.power + self.potionPower
        other.health -= damage
        print(f"{self.name} attacks {other.name} with a potion for {damage} damage!")

    def throw_potion(self, other):
        damage = self.potionPower
        other.health -= damage
        print(f"{self.name} throws a potion at {other.name} for {damage} damage!")

    #overriding
    def speak(self):
        print(f"{self.name} says: 'I am a witch! I brew powerful potions!'")

    #overriding
    def __str__(self):
        return f"{self.name} the Witch (Power: {self.power}, Health: {self.health}, Potion Power: {self.potionPower})"
        