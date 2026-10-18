people = int(input("How many people do you want to invite to the party? "))

if people < 10:
    for _ in range(people):
        name = input("Enter a person's name: ")
        print(f"{name} has been invited")
else:
    print("Too many people.")
