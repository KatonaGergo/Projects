#4-1-2. Feladat
num = []

for i in range(5):
    number = input("Írj ide egy számot: ")
    if number.isnumeric():
        num.append(int(number))
    else:
        print("Nem megfelelő bevitel!")
        break

for number in num:
    if number % 2 == 0:
        print(f"A {number} páros.")
    else:
        print(f"A {number} páratlan.")

#4-2-3. Feladat

canBeDividedByThree = []
canBeDividedByFour = []
canBeDividedByBoth = []
canBeDividedByNone = []

def oszthatosag_vizsgalat(szam):
    if szam % 3 == 0 and szam % 4 == 0:
        canBeDividedByBoth.append(int(szam))
        return "A szám 3-mal és 4-gyel is osztható."
        
    elif szam % 3 == 0:
        canBeDividedByThree.append(int(szam))
        return "A szám csak 3-mal osztható."
    elif szam % 4 == 0:
        canBeDividedByFour.append(int(szam))
        return "A szám csak 4-gyel osztható."
    else:
        canBeDividedByNone.append(int(szam))
        return "A szám sem 3-mal, sem 4-gyel nem osztható."
    
for i in range(3):
    szam = int(input("Adj meg egy egész számot: "))
    eredmeny = oszthatosag_vizsgalat(szam)
    print(eredmeny)

print(f"A 3-mal és 4-gyel is osztható számok: {canBeDividedByBoth}")
print(f"A csak 4-gyel osztható számok: {canBeDividedByFour}")
print(f"A csak 3-mal osztható számok: {canBeDividedByThree}")
print(f"A sem 3-mal, sem 4-gyel nem osztható számok: {canBeDividedByNone}")






