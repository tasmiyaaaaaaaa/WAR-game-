import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}


class Card():
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
        
    def __str__(self):
        return self.rank + ' of ' + self.suit
    
class Deck():
    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(suit,rank))
    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()

class Player():
    def __init__(self, name):
        self.name = name
        self.all_cards = []

    def del_one(self):
        return self.all_cards.pop()
    
    def add_cards(self, new_cards):
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)

    def __str__(self):
        return f'player {self.name} has {len(self.all_cards)} cards.'
    

player_one = Player("One")
player_two = Player("Two")

new_deck = Deck()
new_deck.shuffle()

for i in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())

game_on = True
round_num = 0

while game_on:
    round_num+=1
    print(f"round {round_num}")

    if len(player_one.all_cards) == 0:
        print("Player 1 has no cards left! GAME OVER! BAHAHAHHA LOSERRR")
        print("Player 2 WINSSS!! LESSGOOOO!!")
        game_on = False
        break

    if len(player_two.all_cards) == 0:
        print("Player 2 has no cards left! :(( poor baby))")
        print("Player 1 wins apparently")
        game_on = False
        break

    player_one_cards = []
    player_one_cards.append(player_one.del_one())
    player_two_cards = []
    player_two_cards.append(player_two.del_one())

    war = True

    while war:

        if player_one_cards[-1].value > player_two_cards[-1].value:
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)
            war = False

        elif player_one_cards[-1].value > player_one_cards[-1].value:
            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)
            war = False

        else:
            print("WARRRRRR!!!!")

            if len(player_one.all_cards) < 5:
                print("player 1 is unable to play cuz he got less cards (we need 5 of em babes)")
                print("player 1 is a loser cuz he got skill issue BOOOOOOOOO!!!! ")
                print("PLAYER 2 WINNSSSSS💅💅💅💅💅💅💅💅💅💅💅")
                game_on = False
                break
            
            elif len(player_two.all_cards) < 5:
                print("player 2 is unable to play cuz she got less cards (issok bbg)")
                print("player 2 unfortunately lost, player 1 is a cheater obv cuz he's a *man* ")
                print("player 1 wins *eye roll* wtv ")
                game_on = False
                break
            
            else: #game is on bitches
                for i in range(5):
                    player_one_cards.append(player_one.del_one())
                    player_two_cards.append(player_two.del_one())
