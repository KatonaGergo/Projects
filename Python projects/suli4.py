import statistics

numbers = []
total = ''
mean_value = ''
sorted_list = ''
highest_number = ''


while True:
    num = int(input("Írj ide egy számot (0, ha ki akarsz lépni): "))
    if num == 0: 
        break
    numbers.append(num)

if numbers:
    total = sum(numbers)
    mean_value = statistics.mean(numbers)
    numbers.sort()
    highest_number = numbers[-1]

    
    print("Total:", total)
    print("Mean value:", mean_value)
    print("Sorted list:", numbers)
    print("Highest number:", highest_number)
else:
    print("Nem adtál meg számokat!")
