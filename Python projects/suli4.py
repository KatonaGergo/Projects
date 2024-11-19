import statistics

numbers = []
total = ''
mean_value = ''
sorted_list = ''
highest_number = ''

num = int(input("Írj ide egy számot!"))

while num != 0:
    num = int(input("Írj ide egy számot!"))
    numbers.append(num)

total = sum(numbers)
mean_value = statistics.mean(numbers)
sorted_list = numbers.sort(num)


for i in range(0, len(numbers)):
    if i == (len(numbers)-1):
        print("A legnagyobb szám: "
              + str(numbers[i]))




