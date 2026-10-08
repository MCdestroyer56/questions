num1 = float(input('Enter a number:'))
num2 = float(input('Enter a second number:'))
num3 = float(input('Enter a third number:'))
largest = num1
if largest < num2:
    largest = num2
if largest < num3:
    largest = num3
print('The largest number is:',largest)
    