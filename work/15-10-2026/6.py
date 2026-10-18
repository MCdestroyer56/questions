number = int(input("Enter a number below 50: "))

if number < 50:
    print("You entered:", number)
    for count in range(50, number - 1,-1):
        print(count)
else:
    print("Please enter a number below 50.")
