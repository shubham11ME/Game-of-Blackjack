import random
import art
from replit import clear

def deal_cards():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10,10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare_score(user_score, computer_score):
    if user_score > 21 and computer_score > 21:
        return "You went over. You lose 😤"
    if user_score == computer_score:
        return "Draw 🙃"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif user_score == 0:
        return "Win with a Blackjack 😎"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif computer_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > computer_score:
        return "You win 😃"
    else:
        return "You lose 😤"

def play_game():
    print(art.logo)
    user_card = []
    computer_card = []
    is_game_over = False

    for _ in range(2):
        user_card.append(deal_cards())
        computer_card.append(deal_cards())

    while not is_game_over:
        user_score = calculate_score(user_card)
        computer_score = calculate_score(computer_card)
        print(f"    Your cards: {user_card} and score is: {user_score}")
        print(f"  Computer first card is: {computer_card[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_deal = input("Type 'y' to get another card or 'n' to pass: ")
            if user_deal == 'y':
                user_card.append(deal_cards())
            else:
                is_game_over = True

    while computer_score < 17 and computer_score != 0:
        computer_card.append(deal_cards())
        computer_score = calculate_score(computer_card)

    print(f"    Your final hand is {user_card} and score is {user_score}")
    print(f"  Computer final hand is {computer_card} and score is {computer_score}")
    print(compare_score(user_score, computer_score))

while input("\nDo you want to play Blackjack game? Type 'y' or 'n': ") == 'y':
    clear()
    play_game()