

#1. feladat
input_numbers = []
input_number = int()
for i in range(0, 3):
    input_number = int(input("Írj be számokat!"))
    input_numbers.append(input_numbers)
for i in range(i, len(list1)):
    for j in range(i+1, len(list1)):
        if (list1[i]>list1[j]):
            temp = list1[i]
            list1[i] = list1[j]
            list1[j] = temp



#2. feladat
try_num = 0
while True:
    input_text = input("Írj be szavakat!")
    try_num += 1
    if input_text == "STOP":
        print("A program vége.")
        break
    elif try_num == 5:
        print("Túl sokszor próbálkoztál!")
        break
