intr1 = int(input('Enter the first integer: '))
intr2 = int(input('Enter the second integer: '))
intr3 = int(input('Enter the third integer: '))

if intr1 + intr2 == intr3:
    print(f'{intr1}+{intr2}={intr3}')
elif intr3 + intr2 == intr1:
    print(f'{intr2}+{intr3}={intr1}')
elif intr1 + intr3 == intr2:
    print(f'{intr1}+{intr3}={intr2}')