import random
JAPANESE_NUMBERS = {1: 'ICHI', 2: 'NI', 3: 'SAN', 4: 'SHI', 5: 'GO', 6: 'ROKU'}

print( ''' 
In this traditional Japanese dice game, two dice are rolled in a bamboo
cup by the dealer sitting on the floor. The player must guess if the
dice total to an even (cho) or odd (han) number.
''')
score = 5000

while True:
    while True:
        user_bet_amount = input(f"You have {score} mon. How much do you bet? (or QUIT)")
        if user_bet_amount.isdecimal():
            potential_winnings = int(user_bet_amount) * 2
            break
        else:
            print("Please enter only digits to bet")

    print('''
The dealer swirls the cup and you hear the rattle of dice.
The dealer slams the cup on the floor, still covering the
dice and asks for your bet.
''')

    while True:
        user_bet = input("CHO (even) or HAN (odd)?")
        if user_bet != "CHO" and user_bet != "HAN":
            print("Please enter a valid input")
        else:
            break

    # Dealer picking from dictionary
    dice_one_number = random.randint(1, 6)
    dice_one = JAPANESE_NUMBERS[dice_one_number]
    dice_two_number = random.randint(1, 6)
    dice_two = JAPANESE_NUMBERS[dice_two_number]
    odd_or_even = (dice_one_number + dice_two_number) % 2
    if odd_or_even == 1:
        answer = "HAN"
    elif odd_or_even == 0:
        answer = "CHO"


    print(f'''
The Dealer lifts the cup to reveal:
{dice_one},          {dice_two}
{dice_one_number},   {dice_two_number}
    ''')


    if user_bet == answer:
        print(f"You won! You take {potential_winnings}.")
        score += int(potential_winnings)
    else:
        print(f"You lost, you idiot. You lose {user_bet_amount}")
        score -= int(user_bet_amount)
        if score <= 0:
            print("You ran out of money, game over.")
            break

    play_again = input("Would you like to play again? Y/N")
    if play_again == "Y":
        pass
    elif play_again == "N":
        print(f"Thanks for playing and especially thanks for leaving, your final score was {score}.")
        break
    else:
        print("please enter a valid input")
