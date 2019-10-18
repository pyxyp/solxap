"""--------------------------------------------------------------------
PROGRAM INFO COMMENT
    Shawn Ballinger
    CSC119-004
    Project: cardApp.py
    Description: App that turns playing card notation into the full name
    Dat10/17/19
--------------------------------------------------------------------"""


def main():
    
    ## A program which asks the user to input a playing card short notation
    ## and then outputs the full value and suit
    #


    # Request value and suit inputs from user

    print("")
    print("Please enter short playing card notation (no Jokers!) ")
    cardValueInput = input("Card Value (A, K, Q or J or a number 2 - 10): ")
    cardSuitInput = input("Card suit (H, S, C, or D): ")


    # Process value and assing to printable variable

    if cardValueInput == ("A") :
        longCardValue = ("Ace of")
    elif cardValueInput == ("K") :
        longCardValue = ("King of")
    elif cardValueInput == ("Q") :
        longCardValue ==("Queen of")
    elif cardValueInput == ("J") :
        longCardValue = ("Jack of")
    elif cardValueInput == "2" :
        longCardValue = ("2 of")
    elif cardValueInput == "3" :
        longCardValue = ("3 of")
    elif cardValueInput == "4" :
        longCardValue = ("4 of")
    elif cardValueInput == "5" :
        longCardValue = ("5 of")
    elif cardValueInput == "6" :
        longCardValue = ("6 of")
    elif cardValueInput == "7" :
        longCardValue = ("7 of")
    elif cardValueInput == "8" :
        longCardValue = ("8 of")
    elif cardValueInput == "9" :
        longCardValue = ("9 of")
    elif cardValueInput == "10" :
        longCardValue = ("10 of")


    # Process Suit and assign to printable variable

    if cardSuitInput == "H" :
        longCardSuit = ("Hearts")
    elif cardSuitInput == "S" :
        longCardSuit = ("Spades")
    elif cardSuitInput == "C" :
        longCardSuit = ("Clubs")
    elif cardSuitInput == "D" :
        longCardSuit = ("Diamonds")
    

    # Output print statement naming the card

    print("")
    print("Your card is the" , longCardValue , longCardSuit)
    print("")
    


main()

