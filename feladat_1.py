import random

#3. feladat
paratlan_szam = int()
paratlan_szamok = []

for paratlan_szam in reversed(range(1, 10)):
    if paratlan_szam % 2 == 0:
        continue
    else:
        paratlan_szamok.append(paratlan_szam)

print(paratlan_szamok)


#4. feladat

nums = '0123456789'

valid_input = False

while not valid_input:
    iteration_count = input("Hányszor szeretnéd, hogy írjuk ki a szövegedet?")

    if not iteration_count.isdigit():
        print("Egész számot írj be!")
    elif int(iteration_count) == 0:
        print("Nem ismétlődik a szöveg.")
        valid_input = True
    else:
        iteration_count = int(iteration_count)
        valid_input = True

valid_text = False
while not valid_text:
    user_text = input("Írd ide az ismételni kívánt szöveget: ")
    if any(char in nums for char in user_text):
        print("A szöveg nem tartalmazhat számokat. Kérlek, írj be egy érvényes szöveget!")
    else:
        valid_text = True

for i in range(iteration_count):
    print(user_text)




#6. feladat

random_numbers = []

for i in range(1, 20):
    random_number = random.randint(1, 12)
    if random_number % 3 == 0:
        random_numbers.append(random_number)

print(f"{random_numbers} számok voltak a véletlenszerű, hárommal osztható számok.")

random_numbers_count = len(random_numbers)

print(f"{random_numbers_count} hárommal osztható véletlenszerű szám volt.")

