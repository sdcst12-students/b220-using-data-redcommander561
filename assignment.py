"""We will be generating
* starport type
* check for naval base
* check for scout base
* check for gas giant
* generate a random name ( you can use a random set of numbers or create a library of words/letters.  The name of the system in the Alien movie franchise, fore example, was LV427)
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


DM = 0

for i in range(1):
    rollSize = random.randint(2,12)
    rollAtmosphere = random.randint(2,12)
    rollHydrographics = random.randint(2,12)
    rollPopulation = random.randint(2,12)
    rollGovlvl = random.randint(2,12)
    rollLawlvl = random.randint(2,12)
    rollTechlvl = random.randint(1,6)
    

    starport = random.choice("ABCDEX")
    print(f"Starport: {starport}")

    if starport == "C" or starport == "D" or starport == "E" or starport == "X":
        print("Naval Base: skip")

    else:
        NB = random.choice("nnnnnnyyyyy")

            
        if NB == "n":
            print("Naval Base: No")
        if NB == "y":
            print("Naval Base: Yes")
    

    SB = random.choice("nnnnnyyyyyy")
    if SB == "n":
        print("Scout Base: No")
    if SB == "y":
        print("Scout Base: Yes")
    if starport == "C":
        DM = -1
        print(f"Dice modification: {DM}")
    if starport == "B":
        DM = -2
        print(f"Dice modification: {DM}")
    if starport == "A":
        DM = -3
        print(f"Dice modification: {DM}")
    

    GasG = random.choice("yyyyyyyynnn")
    if GasG == "n":
        print("Gas Giant: No")
    if GasG == "y":
        print("Gas Giant: Yes")

    
    Planetoids = random.choice("yyyyynnnnnn")
    if Planetoids == "n":
        print("Planetoids: No")
    if Planetoids == "y":
        print("Planetoids: Yes")  


    a = random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789")
    b = random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789")
    c = random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789")
    d = random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789")
    e = random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789")
    name = a + b + c + d + e
    print(f"World Name: {name}")

    size = (rollSize -2) + DM
    print(f"Size: {size}")
    
    atmosphere = 0
    
    if size == 0:
        atmosphere = 0
        print(f"Atmosphere: {atmosphere}")

    else: 
        atmosphere = rollAtmosphere-7
        atmosphere = (atmosphere + size) + DM
        print(f"Atmosphere: {atmosphere}")
        if atmosphere == -1:
            DM = -4

    hydrographics = 0
    if size == -1:
            hydrographics = 0
    else:
        hydrographics = ((rollHydrographics -7) + size) + DM
        print(f"Hydrographics: {hydrographics}")
        
    population = (rollPopulation - 2) + DM
    print(f"Population: {population}")

    govLvl = ((rollGovlvl - 7) + population) + DM
    print(f"Government Level: {govLvl}")

    lawLvl = ((rollLawlvl -7) + govLvl) + DM
    print(f"Law Level: {lawLvl}")

    MOD = 0

    if size == 0:
        MOD = MOD + 2
    if atmosphere == 0:
        MOD = MOD + 1
    if govLvl == 0:
        MOD = MOD + 1
    
    if size == 1:
        MOD = MOD + 2
    if atmosphere == 1:
        MOD = MOD + 1
    if population == 1:
        MOD = MOD + 1

    if size == 2:
        MOD = MOD + 1
    if atmosphere == 2:
        MOD = MOD + 1
    if population == 2:
        MOD = MOD + 1

    if size == 3:
        MOD = MOD + 1
    if atmosphere == 3:
        MOD = MOD + 1
    if population == 3:
        MOD = MOD + 1

    if size == 4:
        MOD = MOD + 1
    if population == 4:
        MOD = MOD + 1

    if population == 5:
        MOD = MOD + 1
    if govLvl == 5:
        MOD = MOD + 1

    if hydrographics == 9:
        MOD = MOD + 1
    if population == 9:
        MOD = MOD + 2

    if starport == "A":
        MOD = MOD + 6
    if atmosphere == 10:
        MOD = MOD + 1
    if hydrographics == 10:
        MOD = MOD + 2
    if population == 10:
        MOD = MOD + 4

    if starport == "B":
        MOD = MOD + 4
    if atmosphere == 11:
        MOD = MOD + 1

    if starport == "C":
        MOD = MOD + 2
    if atmosphere == 12:
        MOD = MOD + 1
    
    if atmosphere == 13:
        MOD = MOD + 1
    if govLvl == 13:
        MOD = MOD - 2

    if atmosphere == 14:
        MOD = MOD + 1

    if starport == "X":
        MOD = MOD - 4
     

    techLvl = (rollTechlvl + MOD) + DM
    print(f"Tech Level: {techLvl}")
    
    print(DM)