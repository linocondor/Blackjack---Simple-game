import random
from replit import clear


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def random_card():
    return cards[random.randint(0,12)]



#game function
def blackjack_game():
    #player cards
    player_cards = [random_card(),random_card()]
    current_score = sum(player_cards)

    #computer cards
    computer_cards = [random_card()]

    print(f"    Your cards: {player_cards}, current score: {current_score}")
    print(f"    Computer first card: {computer_cards}")

    continue_playing = True

    while continue_playing:
        play_game = input("Type 'y' if you want another card, and 'n' to pass: ")
        
        if play_game == "y":
            player_cards.append(random_card())
            current_score = sum(player_cards)
            print(f"    Your cards: {player_cards}, current score: {current_score}")
            print(f"    Computer first card: {computer_cards}")

            if sum(player_cards) > 21:
                            
                print(f"    Your final cards: {player_cards}, final score: {current_score}")
                print("Sorry, you loose")
                continue_playing = False

                
        else:
            computer_cards.append(random_card())
            continue_playing = False
            
            while sum(computer_cards) < 17:
                computer_cards.append(random_card())

            computer_score = sum(computer_cards)
            print(f"    Your final cards: {player_cards}, final score: {current_score}")
            print(f"    Computer final's cards: {computer_cards}, final score: {computer_score}")

            if computer_score > 21:
                print("Computer went over. You win 😁")
            
            elif computer_score > current_score:
                print("Computer wins. You loose 😰")
            
            elif computer_score < current_score:
                print("You win 😁")
            
            elif computer_score == current_score:
                print("It's a Draw")

new_game = True
while new_game:
    want_to_play = input("Want to play Blackjack?. Type 'y' or 'n' : ")

    if want_to_play == "y":
        clear()
        blackjack_game()
    else:
        new_game = False



    
    


   
    

            



## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:

## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

