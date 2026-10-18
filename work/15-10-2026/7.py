name = input("Enter your name: ")
number = int(input("Enter a number: "))

if number < 10:
    for _ in range(number):
        print(name)
else:
    for _ in range(3):
        print("Too high")
