import random

def guess(x):
    random_num = random.randint(1,x)
    guess = 0
    while guess!= random_num:
        guess = int(input(f'Guess the the number between 1 and {x}: '))
        if guess < random_num:
            print('Sorry, the number is too low')
        elif guess > random_num:
            print('Sorry, the number is too high')
    print(f'Yay, Congratulations. You have guessed the number {random_num} correctly!')

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        my_guess = random.randint(low,high)
        feedback = input(f'Is {my_guess} too high(h). too low(l), or correct(c)').lower()
        if low == high:
            my_guess = low
        else:    
            if feedback == 'l':
                low = my_guess + 1
            elif feedback == 'h':
                high = my_guess - 1
    print(f'Yay, Congratulations. You have guessed the number {my_guess} correctly!')                

computer_guess(13)
