class Character(): 
    def __init__(self, name, health, level):
        self.name = name
        self.health = health
        self.level = level

    def describe(self): 
        return f'Name: {self.name} | Health: {self.health} | Level: {self.level}'  
    def takeDamge(self, amount):
        self.amount = amount
        self.health -= amount
        return f'{self.name} takes {self.amount} damage. Remaining health: {self.health}'  

ali = Character('Ali', health=50, level=17)
# ahmed = Character('Ahmed')
# print(ali.describe())
# ali.takeDamge(67)
# print(ali.describe())

class Warrior(Character):
    def __init__(self, name, health=100, level=4):
        Character.__init__(self, name, health, level)
        self.health = health
        self.level = level
    def attack(self, target):
        self.target = target
        self.amount = self.level *5
        return f'{self.name} attacks {self.target} for {self.amount} '

nasser = Warrior('Nasser')
print(nasser.attack('mansoor'))

# class Kitten(Cat):
#     def __init__(self, name, age=0, favorite_toy='string'):
#         Cat.__init__(self, name, age)
#         self.favorite_toy = favorite_toy

#     def play(self):
#         print(f'{self.name} plays with {self.favorite_toy}!')
