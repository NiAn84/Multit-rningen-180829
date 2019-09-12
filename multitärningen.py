# Niklas Andersson 180829

import os
import random

print("Hej och välkommen till multitärningen.")
dice = input("Hur många tärningar vill du ha?")
dice = int(dice)
max = input("Hur många sidor vill du att din/dina tärning/tärningar ska ha?")
max = int(max)
min = 1

def roll_dice():
    rull = random.randint(min, max)
    print(f"Kastar tärning {i + 1}, resultatet blev: {rull}")
    kastlista.append(rull)  # Påfyllning av listan efter varje kast.

while True:
    kastlista = []  # Lista som fylls på efter varje kast, detta för att kunna räkna ut medel av kastresultaten.
    for i in range(dice):
        roll_dice() # Kör funktion kasta tärning
    kastlista_res = sum(kastlista)/len(kastlista) # Färdiga medeltalet av kastlistan.
    print(f"Medeltalet bland kastresultaten blev: {kastlista_res}")
    svar = input("Vill du kasta din/dina tärning/tärningar igen? j/n")
    if svar.lower() == "n":
        print("Tack och hej! Ha en fortsatt trevlig dag!")
        os.system("pause")
        break