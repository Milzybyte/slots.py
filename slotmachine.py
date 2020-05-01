import random, time

def wheel():
    return random.choice('777aabbbcccdddd')

def print_row(first, second, third):
    print('[ {} | {} | {} ]'.format(first, second, third,t=time.sleep(.05)), end='\r')

def round():
    for i in range(30):
        if i < 12:
            firstW = wheel()
            secondW = wheel()
            thirdW = wheel()

            print_row(firstW, secondW, thirdW)
        elif i < 25:
            firstW = firstW
            second = wheel()
            third = wheel()

            print_row(firstW, secondW, thirdW)
        else:
            firstW = firstW
            secondW = secondW
            third = wheel()

            print_row(firstW, secondW, thirdW)

    return (firstW, secondW, thirdW)

def ask_to_play():
    global bet
    while(True):
        answer = input("You have $" + str(bet) + ". Would you like to play? y/n ")
        answer = answer.lower().strip()
        if(answer == "y"):
            return True
        elif(answer == "n"):
            print("You ended the game with $" + str(bet) + " in your hand.")
            return False
        else:
            print("incorrect input - type either y or n")

def check_win(a, b, c):
    global bet
    
    if a == 7 and b == 7 and c == 7:
        winnings = 250
    elif a == 7 and b == 7 and (c == "b" or c == "a"):
        winnings = 100
    elif a == "b" and b == "b" and (c == 7 or c == "b"):
        winnings = 40
    elif a == "a" and b == "a" and (c == 7 or c == "a"):
        winnings = 20
    elif a == "c" and b == "c" and c == "c":
        winnings = 15
    elif a == "d" and b == "d":
        winnings = 5
    elif a == "d" and b == "d" and c == "d":
        winnings = 3
    elif a == "d" and b == "d":
        winnings = 2
    else:
        winnings = 0

    if winnings > 0:
        bet += winnings
        print("Congratulations! You just won $" + str(winnings) + "!!!")
    else:
        print("Sorry, for your lose")
        
def play():
    global bet
    want_to_play = ask_to_play()
    while(bet >= 1 and want_to_play == True):
        bet -= 1
        round1 = round()
        a, b, c = round1
        print('[ {} | {} | {} ]'.format(a,b,c))
        check_win(a, b, c)
        
        if bet == 0:
            print("Sorry guy, you ran out of money!")
            break
        
        want_to_play = ask_to_play()
"""
print('''Welcome to play the Slot Machine!
You'll start with $50. You can choose to quit
and cash out after each round. Each round costs $1.
To win you must get one of the following combinations:
7\t7\t7\tpays\t$250
7\t7\tb / a\tpays\t$100
b\tb\tb / 7\tpays\t$40
a\ta\ta / 7\tpays\t$20
c\tc\tc\tpays\t$15
c\tc\t-\tpays\t$5
d\td\td\tpays\t$3
d\td\t-\tpays\t$2''')

"""
bet = 50

play()