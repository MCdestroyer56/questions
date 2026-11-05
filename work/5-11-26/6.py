odd_total = 0
even_total = 0

for i in range(4):
    x = int(input('Enter a number > '))
    if x%2 == 0:
        even_total = even_total + x
    elif x%2 == 1:
        odd_total = odd_total + x
    
print(f'odd total = {odd_total}')
print(f'even total = {even_total}')