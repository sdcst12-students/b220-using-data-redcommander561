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