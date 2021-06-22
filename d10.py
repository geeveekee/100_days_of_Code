import random
print("""
          _____
         |A .  | _____
         | /.\ ||A ^  | _____
         |(_._)|| / \ ||A _  | _____
         |  |  || \ / || ( ) ||A_ _ |
         |____V||  .  ||(_'_)||( v )|
                |____V||  |  || \ / |
                       |____V||  .  |
                              |____V|
 _     _            _    _            _    
| |   | |          | |  (_)          | |   
| |__ | | __ _  ___| | ___  __ _  ___| | __
| '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
| |_) | | (_| | (__|   <| | (_| | (__|   < 
|_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\.
                       _/ |                
                      |__/      



        """)
list_of_cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def generate_cards():
    cards = [random.choice(list_of_cards), random.choice(list_of_cards)]
    return cards

def sum_of_cards(card_list):
    score = 0
    for cards in card_list:
        score += cards
    score = int(score)
    return score

def winner(score1, score2):
    bj_score1 = abs(21-score1)
    bj_score2 = abs(21-score2)
    if bj_score1< bj_score2:
        return True
    else:
        return False

def game():
    player_cards = generate_cards()
    computer_cards = generate_cards()
    print(f"Your cards: {player_cards}")
    print(f"Computer's first card: {computer_cards[0]}")
    choice = input("Type 'y' to get another card, 'n' to pass: ")
    if choice == 'n':
        player_score = sum_of_cards(player_cards)
        computer_score = sum_of_cards(computer_cards)
        print(f"Your final hand: {player_cards} \nComputer's final hand {computer_cards}")
        if winner(player_score, computer_score):
            print("You win!")
        else:
            print("You loose!")
    elif choice == 'y':
        player_cards.append(random.randint(1, 10))
        computer_cards.append(random.randint(1, 10))
        player_score = sum_of_cards(player_cards)
        computer_score = sum_of_cards(computer_cards)

        print(f"Your final hand: {player_cards} \nComputer's final hand {computer_cards}")
        if winner(player_score, computer_score):
            print("You win!")
        else:
            print("You loose!")
        
game()
