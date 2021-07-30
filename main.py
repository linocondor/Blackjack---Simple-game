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



    
 



