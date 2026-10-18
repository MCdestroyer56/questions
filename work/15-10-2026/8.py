total = 0

for i in range(5):
    number = float(input(f"Enter number {i + 1}: "))
    include = input("Do you want to include this number? (yes/no): ").strip().lower()

    if include == "yes":
        total += number

print("Total:", total)
