import random
import time
import math

print("Most egy rasszista teszt elé állítalak téged. Kérem, fáradjon közelebb.")
answer1 = input()
if answer1 == "Rendben":
    print("Nagyszerű. Indul a teszt!")
else:
    print("Nem érdekel, innem már nem menekülhetsz. Indulhat a teszt!")
for loopnum in range(1, 4 + 1, 1):
    print("Rasszista vagy?")
    testanswer = input()
    if testanswer == "Nem":
        pass
    elif testanswer == "Igen":
        print("Tudtam, te geci.")
        break
print("Széthazudod az életed is.")

print("Azt fogjuk ezután játszani, hogy dobunk dobókockával, és ha az én számom nagyobb lesz, mint a tiéd, akkor buzi vagy.")
diceanswer = input()
if diceanswer == "Rendben":
    print("Kezdődjön a játék!")
elif diceanswer == "Nem":
    print("Leszarom. Kezdődjön a játék!")
else:
    print("Leszarom. Kezdődjön a játék!")

min_ertek = 1
max_ertek = 6

max_ertek_valasz = input("Hány oldalú legyen a dobókocka [1-6]")

if max_ertek_valasz != "" and max_ertek_valasz.isnumeric():
    max_ertek = int(max_ertek_valasz)

def dobokocka_eldobasa():
    return random.randint(min_ertek, max_ertek)

def betoltes():
    print("Készülj a szopásra:")
    for szopas in reversed(range(1, 4)):
        time.sleep(0.5)
        print(szopas)

while True:
    valasz = input("Valóban kész vagy a szopásra? [i/n]")
    
    
    if valasz == "i":
        betoltes()
        your_number = dobokocka_eldobasa()
        print(f"A te számod: {your_number}")

        betoltes()
        my_number = dobokocka_eldobasa()
        print(f"Az én számom: {my_number}")

    else:
        print("Leszarom. Megy a dobás.")
        betoltes()
        your_number = dobokocka_eldobasa()
        print(f"A te számod: {your_number}")

        betoltes()
        my_number = dobokocka_eldobasa()
        print(f"Az én számom: {my_number}")

    break


if my_number > your_number:
    print("Há, hülye buzi.")
else:
    print("Ma megúsztad.")

    












