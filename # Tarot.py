# Tarot
# This is a program that draws from a standard Rider-Waite tarot deck, in three spreads.

import random, time, sys

def base10Encode(inputString):
    stringAsBytes = bytes(inputString, "utf-8")
    stringAsBase10 = ""
    for byte in stringAsBytes:
        byteStr = str(byte).rjust(3, '\0') # Pad left with null to aide decoding
        stringAsBase10 += byteStr
    return stringAsBase10

# table of cards.

tarot= ("the Ace of Cups", "the Two of Cups", "the Three of Cups", "the Four of Cups", "the Five of Cups","the Six of Cups","the Seven of Cups","the Eight of Cups","the Nine of Cups","the Ten of Cups"
       "the Page of Cups","the Knight of Cups","the Queen of Cups","the King of Cups",
       "the Ace of Wands", "the Two of Wands", "the Three of Wands", "the Four of Wands", "the Five of Wands","the Six of Wands","the Seven of Wands","the Eight of Wands","the Nine of Wands","the Ten of Wands",
       "the Page of Wands","the Knight of Wands","the Queen of Wands","the King of Wands",
       "the Ace of Pentacles", "the Two of Pentacles", "the Three of Pentacles", "the Four of Pentacles", "the Five of Pentacles","the Six of Pentacles","the Seven of Pentacles","the Eight of Pentacles","the Nine of Pentacles","the Ten of Pentacles",
       "the Page of Pentacles","the Knight of Pentacles","the Queen of Pentacles","the King of Pentacles",
       "the Ace of Swords", "the Two of Swords", "the Three of Swords", "the Four of Swords", "the Five of Swords","the Six of Swords","the Seven of Swords","the Eight of Swords","the Nine of Swords","the Ten of Swords",
       "the Page of Swords","the Knight of Swords","the Queen of Swords","the King of Swords",
       "the Fool","the Magician","the High Priestess","the Empress","the Emperor","the Hierophant","the Lovers","the Chariot","Strength","the Hermit","the Wheel of Fortune","Justice","the Hanged Man","Death",
       "temperance","the Devil","the Tower","the Star","the Moon","the Sun","Judgement","the World")

table = ''

def slowPrint(str):
    for c in str + '\n':
     sys.stdout.write(c)
     sys.stdout.flush()
     time.sleep(3./90)

# Function for drawing a list of cards.
table= ''
def cardDraw(deck, number): 
    global table 
    table= random.sample(deck, number)

def checkIn():
    slowPrint("Are you ready?")
    while True:
        consent = input()
        if consent == "y":
            break
        elif consent == "n":
            slowPrint("That's alright, take your time. If you decide you'd like to leave, type 'exit'.")
        elif consent == 'exit':
            slowPrint("It was lovely having you in. Come again soon.")
            sys.exit
        else:
             "I'm sorry, I didn't catch thet."


# Functions for dealing the cards.

def singleCard():
    slowPrint("You've chosen a single-card spread.")
    slowPrint("This card contains the answer you're looking for.")
    checkIn()
    slowPrint("For you, I've drawn...")
    time.sleep(0.5)
    slowPrint(str(table[0]) + ".")

def tripleCard():
    slowPrint("You've chosen a triple-card spread.")
    slowPrint("I'll draw the three cards for you. These represent your past, present, and the possibilities of your future.")
    slowPrint("")
    checkIn()
    slowPrint("Here you are. The card for your past is " + str(table[0] + "."))
    slowPrint("The card for the present is " + str(table[1]) + ".")
    slowPrint("The final card, the one for your future, is..." + str(table[2]) + '.')

def fiveCardCross():
    slowPrint("This is a the five-card cross spread.")
    slowPrint("These cards represent, in order:")
    slowPrint("Your past, your present, and your future.")
    slowPrint("The the fourth card, placed beneath the main row, tries to explain an underlying reason for your circumstances.")
    slowPrint("The last card, placed above the rest, reveals the potential for your situation:")
    slowPrint("How well it could go, or how poorly.")
    slowPrint("")
    checkIn()
    slowPrint("Alright. Your cards are:")
    slowPrint("The past, represented by " + str(table[0]) + ".")
    slowPrint("Your present moment, " + str(table[1]) + ".")
    slowPrint("And I have drawn " + str(table[2]) + " to represent your future.")
    slowPrint("You can find an underlying reason for your circumstances in " + str(table[3]) + '.')
    slowPrint("And reveal the hidden potential by pondering " + str(table[4]) + ".")

def rectaTheme():
    slowPrint("This is a themed rectangle spread.")
    slowPrint("It can be read in a number of different  ways, but broadly speaking...")
    slowPrint("The the four corners of the rectangle are loosely connected events or circumstances,")
    slowPrint("with a center card representing the overarching theme.")
    slowPrint('')
    checkIn()
    slowPrint("The upper leftmost corner is " + str(table[0]) + ",")
    slowPrint("The upper rightmost corner is " + str(table[1]) + ",")
    slowPrint("The lower righthand corner is " + str(table[2]) + ",")
    slowPrint("The lower left corner is " + str(table[3]) + ",")
    slowPrint("and the theme card in the center is " + str(table[4]) + ".")

# With the deck out of the way, the main body of the program begins.

slowPrint("Hi! You're using a tarot deck built in Python, put together by Hearth.")
slowPrint("You can respond to yes or no questions by typing 'y' or 'n' respectively.")
checkIn()
print('')
slowPrint("Please ask me a question.")
question= input()
time.sleep(0.5)
random.seed(base10Encode(question))     # Sets the seed to the base-10 encoding of the question asked.  

spreadChoice= None
while True:

    print("")
    slowPrint("What spread would you like? Please pick from 1, 3, or 5.")
    time.sleep(0.2)
    slowPrint("If you'd like to arrange your own spread, enter the number zero.")
    time.sleep(0.2)
    slowPrint("If you'd like me to choose for you, type 'Choose for me.'")
    time.sleep(0.2)
    slowPrint("If you'd like to leave, type 'exit'.")
    print("")
    while True:
        spread=input()
        if spread == "0":
                slowPrint("Enter an integer number of cards you'd like for me to draw.")
                time.sleep(0.2)
                slowPrint("These cards will be read in the order I draw them.")
                time.sleep(0.2)
                slowPrint("You may arrange these cards as you see fit.")
                spreadChoice = int(input())
                cardDraw(tarot, spreadChoice)
                slowPrint(str(table))

        elif spread == "1":
                spreadChoice = 1
                cardDraw(tarot, spreadChoice)
                singleCard()
                break

        elif spread == "3":
                spreadChoice = 3
                cardDraw(tarot, spreadChoice)
                tripleCard()
                break

        elif spread == "5":
                spreadChoice = 5
                cardDraw(tarot, spreadChoice)
                slowPrint("If you're looking to uncover hidden potential, respond with 'p'.")
                slowPrint("If you're looking to connect broad themes in your life, respond with 't'.")
                choice5= input()
                if choice5 == 'p':
                    fiveCardCross()
                    break
                if choice5 == 't':
                    rectaTheme()
                    break
                else:
                    slowPrint("Sorry, what was that?")
                

        elif spread == "Choose for me":
                choices = [1, 3, 5]
                spreadChoice = random.choice(choices)
                cardDraw(tarot, spreadChoice)
                if spreadChoice != 1:
                    slowPrint("I've chosen a spread of " + str(spreadChoice) + " cards.")
                    if spreadChoice == 3:
                        tripleCard()
                    if spreadChoice == 5:
                        choices = [fiveCardCross(), rectaTheme()]
                    choices
                    break

                else:
                    slowPrint("I've chosen a single-card spread.")
                    singleCard()
                    break

        elif spread == "exit":
            slowPrint("It was lovely having you in. Come again soon.")
            sys.exit

        else:
            slowPrint("I'm sorry, I didn't catch that. Can you say it again, a little clearer?")
            continue
    
    slowPrint("Are you satisfied with the answers you've received?")
    while True:
        cont= input()
        if cont == 'y':
            print("It's been lovely having you in. Do come back sometime.")
            sys.exit
        elif cont == 'n':
            slowPrint("Do you have another question?")
            quest = input()
            if quest == 'y': 
                print("Ask me.")
                question= input()
                time.sleep(0.5)
                random.seed(base10Encode(question))     # Sets the seed to the base-10 encoding of the question asked.
            elif quest == 'n':
                break
            else:
                slowPrint("I'm sorry, I didn't catch that. Can you say it again, a little clearer?")