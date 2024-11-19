num = int(input("Írj be egy számot!"))

if num % 2 == 0 and num % 3 == 0 and num % 5 ==0:
    print("A szám osztható 2-vel, 3-al, 5-tel.")
elif num % 2 == 0 and num % 3 == 0:
    print("A szám oszható 2-vel, 3-mal")
elif num % 2 == 0 and num % 5 == 0:
    print("A szám oszható 2-vel, 5-tel")
elif num % 3 == 0 and num % 5 == 0:
    print("A szám osztható 3-mal, 5-tel")
else:
    print("A szám nem osztható 3-mal, 2-vel, 5-tel")

#évszak

num = int(input("Írjon be egy évszaknak a számát!"))

tavasz = [3, 4, 5]
tél = [1, 2, 12]
nyár = [6, 7 ,8]
ősz = [9, 10, 11]

if num in tavasz:
    print("Tavaszi hónap")
if num in tél:
    print("Téli hónap")
if num in nyár:
    print("Nyári hónap")
if num in ősz:
    print("Őszi hónap")

