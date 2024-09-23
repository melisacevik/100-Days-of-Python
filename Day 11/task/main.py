#Oyun kuralları
# 1. Elimizdeki kartların toplamı 21'den fazlaysa buna Bust denir ve direkt kaybetmiş olursun.
# 2. Kartların sayılma şekli => 2'den 20'ye kadar olan tüm kartların nominal değerleri olarak sayılır.
# 3. Vale, Kız, Papaz => 10 sayılır.
# 4. As => toplama 1 eklenir veya 11 olarak sayılabilir
# 21'i geçip geçmediğine göre asın hangi değeri temsil etmek istediğine karar verebiliriz
# Kurallara göre dağıtıcının elinde 16 dahil daha küçük bir el varsa; bir kart daha alması gerekiyor
#direkt 21 gelirse => Blackjack, kazanıyosun. 21 in altındaysa karşı taraf veya üstündeyse her türlü ben kazanıyorum
# o 25 sen 17 isen sen kazanıyosun

import random

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0 #blackjack

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(u_score, c_score):
    """Compares the user score u_score against the computer score c_score."""
    if u_score == c_score:
        return "Draw 🙃"
    elif c_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif u_score == 0:
        return "Win with a Blackjack 😎"
    elif u_score > 21:
        return "You went over. You lose 😭"
    elif c_score > 21:
        return "Opponent went over. You win 😁"
    elif u_score > c_score:
        return "You win 😃"
    else:
        return "You lose 😤"

user_cards = []
computer_cards = []
is_game_over = False
computer_score = -1
user_score = -1

for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

while not is_game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"Your cards: {user_cards}, current score: {user_score}")
    print(f"Computer's first cards: {computer_cards[0]}")

    if user_score  == 0 or computer_score == 0 or user_score > 21:
        is_game_over = True
    else:
        user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
        if user_should_deal == "y":
            user_cards.append(deal_card())
        else:
            is_game_over = True

while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

print(compare(user_score, computer_score))