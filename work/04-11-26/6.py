secret = '7'
secret = int(secret
             )
guess = int(input('Guess the secret number: '))

if guess == (secret):
    print('Bingo! Correct answer')

elif guess == 8 or guess == 6:
    print('Close enough to the correct answer')

else:
    print('Not close enough')