class Character(): 
    def __init__(self, name, health, level):
        self.name = name
        self.health = health
        self.level = level

    def describe(self): 
        return f'Name: {self.name} | Health: {self.health} | Level: {self.level}'  
        
    def takeDamge(self, amount):
        self.health -= amount
        return f'{self.name} takes {amount} damage. Remaining health: {self.health}'  

class Warrior(Character):
    allWarriors = []
    
    def __init__(self, name, health=100, level=4):
        Character.__init__(self, name, health, level)
        Warrior.allWarriors.append(self)
        
    def attack(self, target):
        amount = self.level * 5
        target.takeDamge(amount)
        return f'{self.name} attacks {target.name} for {amount} damage'
        
    @staticmethod
    def listWarriors():
        print(f"{len(Warrior.allWarriors)} warriors available: ")
        for warrior in Warrior.allWarriors:
            print(f"- {warrior.name} (Health: {warrior.health})") 

class Healer(Character):
    def __init__(self, name, health=100, level=3):
        Character.__init__(self, name, health, level)
        
    def heal(self, target):
        if target == self:
            return f"{self.name} attempts to heal himself, but it is blocked!"
            
        amount = self.level * 4 
        target.health += amount
        return f'{self.name} heals {target.name} for {amount} health. Remaining health: {target.health}'


w1 = Warrior("Nawaf", health=90)
w2 = Warrior("Mujtaba", health=120)
h1 = Healer("Fadhel")
c1 = Character("Abdulrahman", 100, 2) 

print("Battle Starts")
print(w1.attack(c1))  
print(w2.attack(c1))  
print(h1.heal(c1))    
print(w2.attack(h1))  
print(h1.heal(h1))    

print("\nWarrior Statuses")
Warrior.listWarriors()