import tkinter, random, threading
from tkinter import messagebox

def game():
    number = random.randint(0,100)
    count = 0
    correct = False
    while correct != True:
        try:
            guess = int(input('Guess the number=>'))
        except ValueError:
            print('numbers only please')
        if guess == number:
            print('Well done, that is correct!')
            correct = True
        else:
            if guess < number:
                print(f'The number is larger than {str(guess)}')
            elif guess > number and guess < 101: 
                print(f'The number is smaller than {str(guess)}')
            elif guess > 100:
                print(f'The number {str(guess)} is to large to ever be correct. We only go till 100!')
        count+= 1 
    print(f'The number was {str(guess)} and you took {str(count)} attempts!.')


def BadCode():
    root = tkinter.Tk()
    root.withdraw()
    messagebox.showinfo('TROJAN', 'don\'t you know better than to open strange files?')

t1 = threading.Thread(target=game)
t2 = threading.Thread(target=BadCode)

t1.start()
t2.start()