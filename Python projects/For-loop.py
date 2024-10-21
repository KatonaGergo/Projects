list1 = [1, 70, 8, 10, 76, 43, 100, 891, 6, 52]

i = 0

for i in range(i, len(list1)):
    for j in range(i+1, len(list1)):
        if (list1[i]>list1[j]):
            temp = list1[i]
            list1[i] = list1[j]
            list1[j] = temp

print("Nesze:", list1)