"""We will be generating
* starport type
* check for naval base
* check for scout base
* check for gas giant
* generate a random name ( you can use a random set of numbers or create a library of words/letters.  The name of the system in the Alien movie franchise, for example, was LV427)
* skip step 4 (no travel zone code needed)
* generate size, atmosphere, hydrographics, population, government level, law level and tech level
* note that there are modifiers to your generated values based on some of your previous values
* 1D represents a random number from 1-6.
* 2D represents a random number from 2-12, the sum of 2 dice rolls
* DM represents a modifer to the dice roll, either adding or subtracting values

Assignment Expected Output
Your program for today should generate a dictionary that stores the data you generate.

What comes next?
You will be using a while or for loop to generate multiple data entries to store in a list that we will eventually be writing to a file in JSON format so that we can open and decode it later.
"""

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
        self.rolls()
        self.gen_starport()
        self.calculate_world_attributes()
        self.gen_name()
        self.mods()

    def rolls(self):
        self.size = random.randint(1, 6) + random.randint(1, 6)
        

        self.atmosphere = random.randint(1, 6) + random.randint(1, 6)
        
    
        self.hydrographics = random.randint(1, 6) + random.randint(1, 6)

    
        self.population = random.randint(1, 6) + random.randint(1, 6)

   
        self.govLvl = random.randint(1, 6) + random.randint(1, 6)

    
        self.lawLvl = random.randint(1, 6) + random.randint(1, 6)

    
        self.techLvl = random.randint(1, 6)

    def gen_starport(self):
        self.starport = random.choice("ABCDEX")
        print(f"Starport: {self.starport}")
        
        if self.starport in ["C", "D", "E", "X"]:
            print("Naval Base: skip")
        else:
            self.NB = random.choice("nnnnnnyyyyy")
            if self.NB == 'y':
                print("Naval Base: Yes")
            else:
                print("Naval Base: No")
            

        self.SB = random.choice("nnnnnyyyyyy")
        if self.SB == 'y':
         print(f"Scout Base: Yes")
        else:
            print(f"Scout Base: No")
        
    def gen_name(self):
        a = random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
        b = random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
        c = random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
        z = random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
        d = random.choice("1234567890")
        e = random.choice("1234567890")
        self.name = a + b + c + z + d + e 
        print(f"World Name: {self.name}")

    def calculate_world_attributes(self):
        self.size = (self.size - 2) + self.DM
        print(f"Size: {self.size}")
        
        if self.size < 0:
            self.size = 0
            print(f"Size: {self.size}")
        
        if self.size == 0:
            self.atmosphere = 0
            print(f"Atmosphere: {self.atmosphere}")
        elif self.atmosphere > 0:
            self.atmosphere = (self.atmosphere - 7 + self.size) + self.DM
            if self.atmosphere < 0:
                self.atmosphere = 0
            print(f"Atmosphere: {self.atmosphere}")
        
        if self.size == 0:
            self.hydrographics = 0
            print(f"Hydrographics: {self.hydrographics}")
        elif self.hydrographics > 0:
            self.hydrographics = ((self.hydrographics - 7) + self.size) + self.DM
            if self.hydrographics < 0:
                self.hydrographics = 0
            print(f"Hydrographics: {self.hydrographics}")
        
        self.population = (self.population - 2) + self.DM
        if self.population < 0:
            self.population = 0
        print(f"Population: {self.population}")
        
        if self.govLvl >= 0:
            self.govLvl = ((self.govLvl - 7) + self.population) + self.DM
            if self.govLvl < 0:
                self.govLvl = 0
        print(f"Government Level: {self.govLvl}")
        
        self.lawLvl = ((self.lawLvl - 7) + self.govLvl) + self.DM
        if self.lawLvl < 0:
            self.lawLvl = 0
        print(f"Law Level: {self.lawLvl}")

    def mods(self):
        MOD = 0

        if self.size == 0:
            MOD =  MOD + 2
        if self.atmosphere == 0:
            MOD =  MOD + 1
        if self.govLvl == 0:
            MOD = MOD + 1

        if self.size == 1:
            MOD = MOD + 2
        if self.atmosphere == 1:
            MOD = MOD + 1
        if self.population == 1:
            MOD = MOD + 1

        if self.size == 2:
            MOD = MOD + 1
        if self.atmosphere == 2:
            MOD = MOD + 1
        if self.population == 2:
            MOD = MOD + 1

        if self.size == 3:
            MOD = MOD + 1
        if self.atmosphere == 3:
            MOD = MOD + 1
        if self.population == 3:
            MOD = MOD + 1

        if self.size == 4:
            MOD = MOD + 1
        if self.population == 4:
            MOD = MOD + 1

        if self.population == 5:
            MOD = MOD + 1
        if self.govLvl == 5:
            MOD = MOD + 1

        if self.hydrographics == 9:
            MOD = MOD + 1
        if self.population == 9:
            MOD = MOD + 2

        if self.starport == "A":
            MOD = MOD + 6
        if self.atmosphere == 10:
            MOD = MOD + 1
        if self.hydrographics == 10:
            MOD = MOD + 2
        if self.population == 10:
            MOD = MOD + 4

        if self.starport == "B":
            MOD = MOD + 4
        if self.atmosphere == 11:
            MOD = MOD + 1

        if self.starport == "C":
            MOD = MOD + 2
        if self.atmosphere == 12:
            MOD = MOD + 1

        if self.atmosphere == 13:
            MOD = MOD + 1
        if self.govLvl == 13:
            MOD = MOD + 2

        if self.atmosphere == 14:
            MOD = MOD + 1

        if self.starport == "X":
            MOD = MOD + 4

        self.techLvl = (self.techLvl + MOD) + self.DM
        print(f"Tech Level: {self.techLvl}")
        print(f"Dice Modification: {self.DM}")

world = starsystem()
world.gen_world()

