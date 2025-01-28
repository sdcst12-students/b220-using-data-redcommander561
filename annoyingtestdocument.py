import random


class starsystem:
    def __init__(self):
        self.DM = 0
        self.name = ""
        self.size = 0
        self.atmosphere = 0
        self.hydrographics = 0
        self.population = 0
        self.govLvl = 0
        self.lawLvl = 0
        self.techLvl = 0
        self.starport = ""
        self.NB = ""
        self.SB = ""
        self.GasG = ""
        self.Planetoids = ""
    
    def gen_world(self):
        self.roll_size()
        self.roll_atmosphere()
        self.roll_hydro()
        self.roll_pop()
        self.roll_gov()
        self.roll_law()
        self.roll_tech()
        self.gen_starport()
        self.calculate_world_attributes()
        self.gen_name()
        self.mods()

    def roll_size(self):
        self.size = random.randint(2, 12)

    def roll_atmosphere(self):
        self.atmosphere = random.randint(2, 12)

    def roll_hydro(self):
        self.hydrographics = random.randint(2, 12)

    def roll_pop(self):
        self.population = random.randint(2, 12)

    def roll_gov(self):
        self.govLvl = random.randint(2, 12)

    def roll_law(self):
        self.lawLvl = random.randint(2, 12)

    def roll_tech(self):
        self.techLvl = random.randint(1, 6)

    def gen_starport(self):
        self.starport = random.choice("ABCDEX")
        print(f"Starport: {self.starport}")
        
        if self.starport in ["C", "D", "E", "X"]:
            print("Naval Base: skip")
        else:
            self.NB = random.choice("nnnnnnyyyyy")
            print(f"Naval Base: {'Yes' if self.NB == 'y' else 'No'}")

        self.SB = random.choice("nnnnnyyyyyy")
        print(f"Scout Base: {'Yes' if self.SB == 'y' else 'No'}")

    def gen_name(self):
        a = random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789")
        b = random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789")
        c = random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789")
        d = random.choice("1234567890")
        e = random.choice("1234567890")
        self.name = a + b + c + d + e 
        print(f"World Name: {self.name}")

    def calculate_world_attributes(self):
        self.size = (self.size - 2) + self.DM
        print(f"Size: {self.size}")

        if self.size == 0:
            self.atmosphere = 0
            print(f"Atmosphere: {self.atmosphere}")
        else:
            self.atmosphere = (self.atmosphere - 7 + self.size) + self.DM
            print(f"Atmosphere: {self.atmosphere}")

        if self.size == -1:
            self.hydrographics = 0
        else:
            self.hydrographics = ((self.hydrographics - 7) + self.size) + self.DM
            print(f"Hydrographics: {self.hydrographics}")

        self.population = (self.population - 2) + self.DM
        print(f"Population: {self.population}")

        self.govLvl = ((self.govLvl - 7) + self.population) + self.DM
        print(f"Government Level: {self.govLvl}")

        self.lawLvl = ((self.lawLvl - 7) + self.govLvl) + self.DM
        print(f"Law Level: {self.lawLvl}")

    def mods(self):
        MOD = 0

        if self.size == 0:
            MOD += 2
        if self.atmosphere == 0:
            MOD += 1
        if self.govLvl == 0:
            MOD += 1

        if self.size == 1:
            MOD += 2
        if self.atmosphere == 1:
            MOD += 1
        if self.population == 1:
            MOD += 1

        if self.size == 2:
            MOD += 1
        if self.atmosphere == 2:
            MOD += 1
        if self.population == 2:
            MOD += 1

        if self.size == 3:
            MOD += 1
        if self.atmosphere == 3:
            MOD += 1
        if self.population == 3:
            MOD += 1

        if self.size == 4:
            MOD += 1
        if self.population == 4:
            MOD += 1

        if self.population == 5:
            MOD += 1
        if self.govLvl == 5:
            MOD += 1

        if self.hydrographics == 9:
            MOD += 1
        if self.population == 9:
            MOD += 2

        if self.starport == "A":
            MOD += 6
        if self.atmosphere == 10:
            MOD += 1
        if self.hydrographics == 10:
            MOD += 2
        if self.population == 10:
            MOD += 4

        if self.starport == "B":
            MOD += 4
        if self.atmosphere == 11:
            MOD += 1

        if self.starport == "C":
            MOD += 2
        if self.atmosphere == 12:
            MOD += 1

        if self.atmosphere == 13:
            MOD += 1
        if self.govLvl == 13:
            MOD -= 2

        if self.atmosphere == 14:
            MOD += 1

        if self.starport == "X":
            MOD -= 4

        self.techLvl = (self.techLvl + MOD) + self.DM
        print(f"Tech Level: {self.techLvl}")
        print(f"Dice Modification: {self.DM}")


world = starsystem()
world.gen_world()
