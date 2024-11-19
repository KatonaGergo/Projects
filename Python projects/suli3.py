
num = int(input("Írd ide a kezdőértéket!"))
num2 = int(input("Írd ide a végsőértéket!"))

number = num < num2

while num < number < num2:
    if number % 3 == 0:
        print(number)

