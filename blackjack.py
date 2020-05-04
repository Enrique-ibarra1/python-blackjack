from deckandcards import Deck, Card


def player_sum(hand):
    player_total = 0
    for playercard in hand:
        if playercard.rank == 'Jack':
            playercard.value = 10
        if playercard.rank == 'Queen':
            playercard.value == 10
        if playercard.rank == 'King':
            playercard.value == 10
        player_total = player_total + playercard.value
        if player_total > 21:
            print("You have overdrawn, bust.")
    print(f"the players total is {player_total}")
    return player_total

def dealer_sum(hand):
    dealer_total = 0
    for dealercard in hand:
        if dealercard.rank == "Jack":
            dealercard.value = 10
        if dealercard.rank == "Queen":
            dealercard.value = 10
        if dealercard.rank == "King":
            dealercard.value = 10
        dealer_total = dealer_total + dealercard.value
    print(f"the dealers total is {dealer_total}")
    return int(dealer_total)

def dealer_check(total, hand2):
    dealer_total = total
    if dealer_total <= 16:
        print("Dealer Hits..")
        dealer_hand.append(new_deck.deal_card())
        for dealercard in hand2:
            if dealercard.rank == "Jack":
                dealercard.value = 10
            if dealercard.rank == "Queen":
                dealercard.value = 10
            if dealercard.rank == "King":
                dealercard.value = 10
            dealer_total = dealer_total + dealercard.value
            print(f"the dealers new total is {dealer_total}")
            if dealer_total > 21:
                print("Dealer has overdrawn, you win")
            return dealer_total
    
def compare_totals(player_total, dealer_total):
    if player_total > 21:
        print("you bust")
        print("dealer wins")
        return
    if dealer_total == 21:
        print("dealer busts")
        return
    if dealer_total == 21 and player_total == 21:
        print("You tie")
        return
    if player_total == 21:
        print("You win")
        return
    if player_total > dealer_total and player_total < 22:
        print("You win")
    
def ace_decide(hand1):
    for playercard in hand1:
        if playercard.value == 1:
            ace_picker = input("Is your Ace a 1 or 11: ")
            if int(ace_picker) == 11:
                print("changing to 11")
                playercard.value = 11
            if ace_picker == 1:
                print("staying at 1")

print("welcome to blackjack")
game_start = input("Start Game? y/n: ")
if game_start == "y":
    new_deck = Deck()
    new_deck.shuffle_deck
    dealer_hand = []
    player_hand = []
    player_hand.append(new_deck.deal_card())
    # player_hand.append(Card('heart', 1))
    player_hand.append(new_deck.deal_card())
    dealer_hand.append(new_deck.deal_card())
    dealer_hand.append(new_deck.deal_card())
    print(f"players hand is {player_hand}")
    print(f"dealers hand is {dealer_hand}")
    ace_decide(player_hand)
    hit_or_stay = input("Hit or stay? hit/stay: ")
    if hit_or_stay == "hit":
        player_hand.append(new_deck.deal_card())
        print(f"players hand is {player_hand}")
        hit_or_stay = input("hit or stay? hit/stay: ")
    if hit_or_stay == "stay":
        a = player_sum(player_hand)
        b = dealer_sum(dealer_hand)
        if b <= 16:
            c = dealer_check(b, dealer_hand)
            compare_totals(a,c)
        else:
            compare_totals(a,b)
        

if game_start == "n":
    print("What are you even doing here then get out")
