roses = int(input('How many roses would you like: '))
tulips = int(input('How many tulips would you like: '))
chrysanthemums = int(input('How many chrysanthemums would you like: '))

bouqet = 2
roses_price = 0
tulips_price = 0
chrysanthemums_price = 0

bouqet = int(bouqet)
roses_price = int(roses_price)
tulips_price = int(tulips_price)
chrysanthemums_price = int(chrysanthemums_price)

season = input('Enter the season of the year: ')

if season == 'spring' or season == 'summer':
    roses_price = 4.10
    tulips_price = 2.50
    chrysanthemums_price = 2.00
    
elif season == 'autumn' or season == 'winter':
    roses_price = 4.50
    tulips_price = 4.15
    chrysanthemums_price = 3.75

roses_price = roses_price*roses_price
tulips_price = tulips_price*tulips
chrysanthemums_price = chrysanthemums_price*chrysanthemums
    
tot_price = roses_price + tulips_price + chrysanthemums_price + bouqet
print(f'The total price of your bouqet is €{tot_price}')