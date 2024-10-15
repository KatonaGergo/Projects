import statistics

numbers = []
total = ''
mean_value = ''
sorted_list = ''
highest_number = ''

# Get input from user in a loop
while True:
    num = int(input("Írj ide egy számot (0 to finish): "))
    if num == 0:  # Exit condition
        break
    numbers.append(num)

if numbers:  # Ensure the list is not empty
    total = sum(numbers)
    mean_value = statistics.mean(numbers)
    numbers.sort()  # Sort the list in place
    highest_number = numbers[-1]  # The last element after sorting

    # Output results
    print("Total:", total)
    print("Mean value:", mean_value)
    print("Sorted list:", numbers)
    print("Highest number:", highest_number)
else:
    print("No numbers were entered.")




