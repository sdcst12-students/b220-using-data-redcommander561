import random

print("roll the dice to determine your actions: ")
for i in range(1):
    d1 = random.randint(1,6)
    d2 = random.randint(1,6)

    roll = d1 + d2

    print(f"you rolled {d1} and {d2}! your total is {roll}")

    starport = random.choice("ABCDEX")
    print(f"starport: {starport}")

    if starport == "C" or  starport == "D" or  starport =="E" or  starport== "X":
        print("naval base: skip")
    else:
        NB = random.choice("nnnnnnyyyyy")
        if NB =="n":
            print("Naval base: no")
        if NB == "y":
            print("Naval base: yes")
    
    SB = random.choice("nnnnnnyyyyy")
    if SB =="n":
        print("Scout base: no")
    if SB == "y":
        print("Scout base: yes")

    if starport == "C":
        DM = roll -1
        print(f"dice modification: {DM}")
    if starport == "B":
        DM = roll -2
        print(f"dice modification: {DM}")
    if starport == "A":
        DM = roll -3
        print(f"dice modification: {DM} ")

    GSG = random.choice("yyyyyyyynnn")
    if GSG =="n":
        print("Gas Giant: no")
    if GSG == "y":
        print("Gas Giant: yes")

    PT = random.choice("yyyyynnnnnn")
    if PT == "n":
        print("Planetoids: no")
    if PT == "y":
        print("Planetoids: yes ")

    A = random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    B = random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    C = random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    D = random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    E = random.choice("1234567890901903284803445")

    name = A + B + C + D + E 
    print(f"world name: {name}")

    size = roll - 2
    print(f"Size: {size}")

    atmosphere = 0
    if size == 0:
        atmosphere = 0 
        print(f"Atmosphere: {atmosphere}")
    else:
        atmosphere = roll - 7
        atmosphere = atmosphere + size
        print(f"Atmosphere: {atmosphere}")

    population = roll - 2
    print(f"Population: {population}")

    gov = (roll - 7) + population
    print(f"Government level: {gov}")

    law = (roll - 7) + gov
    print(f"Law level: {law}")

    
    techbase = roll - 2  

    
    if gov > 6:  
        techbase + 2
    if law > 6:  
        techbase + 1
    if population > 5:  
        techbase + 1
    
    
    tech = max(0, min(techbase, 15))

    print(f"Tech Level: {tech}")

