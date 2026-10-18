direction = input("Which direction do you want to count (up or down)? ").strip().lower()

if direction == "up":
    top_number = int(input("Enter the top number: "))
    for number in range(1, top_number + 1):
        print(number)
elif direction == "down":
    number = int(input("Enter a number below 20: "))
    if number < 20:
        for count in range(20, number - 1, -1):
            print(count)
    else:
        print("Please enter a number below 20.")
else:
    print("I don't understand")
