import random

abc = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$_-.%/^()[]{}'


jelszo = input("Adj meg egy jelszót! (a-z)")

for letter in jelszo:
    if letter not in abc:
        print("Nem megfelelő bevitel! (a-z)")
        exit()

probalkozasok_szama = 0
probalt_jelszo = ""

while probalt_jelszo != jelszo:
    probalt_jelszo = ""
    probalkozasok_szama += 1

    for i in range(len(jelszo)):
        probalt_jelszo += random.choice(abc)

print(f"A jelszó {probalt_jelszo} volt. {probalkozasok_szama} próbálkozásba került feltörni.")
