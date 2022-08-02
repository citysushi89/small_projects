import random, sys, time

# TODO: NOT READY
money = 5000
print(f"Money: ${money}")
bet = input("How much do you want to bet? (1-5000, or QUIT) ")

print(f"You bet: ${bet}")

# Set up the constants:
HEARTS = chr(9829) # Character 9829 is '♥'.
DIAMONDS = chr(9830) # Character 9830 is '♦'.
SPADES = chr(9824) # Character 9824 is '♠'.
CLUBS = chr(9827) # Character 9827 is '♣'.
# (A list of chr codes is at https://inventwithpython.com/charactermap)
BACKSIDE = 'backside'
starting_score = 0
game_is_on = True
player_is_receiving = True
dealer_is_receiving = True
dealing = True
# hitting = True
global player_score, dealer_score
player_score = 0
dealer_score = 0

possible_cards = [2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9,
                  10, 10, 10, 10, "J", "J", "J", "J", "Q", "Q", "Q", "Q", "K", "K", "K", "K", "A", "A", "A", "A"]
removed_cards = 1
random_card = random.randint(0, len(possible_cards) - removed_cards)


def get_score(input_list, score):
    score = 0
    for item in input_list:
        if type(item) == int:
            score += item
        elif item == "J" or "Q" or "K":
            score += 10
        elif item == "A" and score < 12:
            score += 11
        elif item == "A" and score > 21:
            score += 1
    return score


while dealing:
    # deal and count and print dealers cards
    dealer_cards = []

    new_card = possible_cards[random.randint(0, len(possible_cards) - removed_cards)]
    dealer_cards.append(new_card)
    possible_cards.remove(new_card)
    removed_cards += 1
    new_card = possible_cards[random.randint(0, len(possible_cards) - removed_cards)]
    dealer_cards.append(new_card)
    possible_cards.remove(new_card)
    removed_cards += 1

    print(f"Dealer Cards: [?, {dealer_cards[1]}]")
    dealer_score = get_score(dealer_cards, starting_score)
    # Set up global declaration of player_score so it remains consistent

    if dealer_score == 21:
        print("Dealer Blackjack, Game Over!")
        dealing = False
        break

    while player_is_receiving:
        # Dealing User Cards and resetting score
        dealer_score = 0
        player_score = 0
        player_cards = []
        new_card = possible_cards[random.randint(0, len(possible_cards) - removed_cards)]
        player_cards.append(new_card)
        possible_cards.remove(new_card)
        removed_cards += 1
        new_card = possible_cards[random.randint(0, len(possible_cards) - removed_cards)]
        player_cards.append(new_card)
        possible_cards.remove(new_card)
        removed_cards += 1

        print(f"Player Cards: {player_cards}")
        player_score = get_score(player_cards, starting_score)
               
        while player_is_receiving:
            user_choice = input("What would you like to do? S,H,DD")
            if user_choice == "DD":
                new_card = possible_cards[random.randint(0, len(possible_cards) - removed_cards)]
                possible_cards.remove(new_card)
                removed_cards += 1
                player_cards.append(new_card)
                print(f"Player Cards {player_cards}")
                player_score = get_score(player_cards, player_score)
                if player_score > 21:
                    # break player loop and go to the end
                    dealing = False
                    break
                elif player_score < 21:
                    pass

            elif user_choice == "H":
                # while hitting:
                new_card = possible_cards[random.randint(0, len(possible_cards) - removed_cards)]
                player_cards.append(new_card)
                print(f"Player Cards {player_cards}")
                player_score = get_score(player_cards, player_score)
                if player_score > 21:
                    print("Busted!")
                    dealer_is_receiving = False
                    player_is_receiving = False
                    break
                elif player_score == 21:
                    print("21! The dealer still gets a shot though")
                    player_is_receiving = False
                    break
                elif player_score < 21:
                    continue
                    # user_choice_after_hit = input("What would you like to do? S or H?")
                    # if user_choice_after_hit == "H":
                    #     hitting = True
                    # elif user_choice_after_hit == "S":
                    #     hitting = False
                    #     player_is_receiving = False
                    #     break

            elif user_choice == "S":
                hitting = False
                player_is_receiving = False
                break
            else:
                print("invalid input, please try again.")


    # Checking dealer cards, hitting if under 17
    def dealer_price_update(dealer_cards, dealer_score):
        print(f"Dealer cards are: {dealer_cards}")
        # TODO delete the below
        print(dealer_score)
        return dealer_score


    while dealer_is_receiving:
        time.sleep(1)
        if dealer_score > 21:
            print("dealer score too high")
            dealer_score = dealer_price_update(dealer_cards, new_score)
            dealer_is_receiving = False
            # dealing = False
            break
        elif dealer_score >= 18 and "A" in dealer_cards:
            # This will be where you account for hitting on a soft 17
            dealer_is_receiving = False
            # dealing = False
            break
        elif dealer_score >= 17:
            new_score = get_score(dealer_cards, dealer_score)
            dealer_score = dealer_price_update(dealer_cards, new_score)
            dealer_is_receiving = False
            # dealing = False
            break
        elif dealer_score < 17:
            print("Dealer Hits")
            new_card = possible_cards[random.randint(0, len(possible_cards) - removed_cards)]
            dealer_cards.append(new_card)
            new_score = get_score(dealer_cards, dealer_score)
            print(new_score)
            dealer_score = dealer_price_update(dealer_cards, new_score)
    

    if dealer_score == player_score:
        print(f"DEALER SCORE: {dealer_score}")
        print(f"PLAYER SCORE: {player_score}")
        print(f"Push. You still have ${money}")
        continue_or_not = input("Would you like to play again? Y/N")
        if continue_or_not == "Y":
            player_is_receiving = True
            dealer_is_receiving = True
            dealer_score = 0
            player_score = 0
            continue
        else:
            player_is_receiving = False
            dealer_is_receiving = False
            print(f"Thanks for playing, you ended with {money}")
            break

    elif dealer_score > player_score and dealer_score < 22:
        print(f"DEALER SCORE: {dealer_score}")
        print(f"PLAYER SCORE: {player_score}")
        print("Dealer won, better luck next time.")
        print(f"You lost ${bet}.")
        money = money - int(bet)
        print(f"You now have ${money}")
        continue_or_not = input("Would you like to play again? Y/N")
        if continue_or_not == "Y":
            player_is_receiving = True
            dealer_is_receiving = True
            dealer_score = 0
            player_score = 0
            continue
        else:
            player_is_receiving = False
            dealer_is_receiving = False
            dealer_score = 0
            player_score = 0
            print(f"Thanks for playing, you ended with {money}")
            break

    elif player_score > 21:
        print(f"DEALER SCORE: {dealer_score}")
        print(f"PLAYER SCORE: {player_score}")
        print("Dealer won, you busted, better luck next time.")
        print(f"You lost ${bet}.")
        money = money - int(bet)
        print(f"You now have ${money}")
        continue_or_not = input("Would you like to play again? Y/N")
        if continue_or_not == "Y":
            player_is_receiving = True
            dealer_is_receiving = True
            dealer_score = 0
            player_score = 0
            continue
        else:
            player_is_receiving = False
            dealer_is_receiving = False
            dealer_score = 0
            player_score = 0
            print(f"Thanks for playing, you ended with {money}")
            break
            

    elif player_score > dealer_score and player_score < 21:
        print(f"DEALER SCORE: {dealer_score}")
        print(f"PLAYER SCORE: {player_score}")
        print("You won!")
        money = money + int(bet)
        print(f"You now have ${money}")
        continue_or_not = input("Would you like to play again? Y/N")
        if continue_or_not == "Y":
            player_is_receiving = True
            dealer_is_receiving = True
            dealer_score = 0
            player_score = 0
            continue
        else:
            player_is_receiving = False
            dealer_is_receiving = False
            dealer_score = 0
            player_score = 0
            print(f"Thanks for playing, you ended with {money}")
            break
            

