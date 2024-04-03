import random

class Card:
    def __init__(self, suit, rank):
        self.rank = rank
        self.suit = suit
    
    def __str__(self):
        return f"{self.rank['rank']} of {self.suit}"

class Deck:
    def __init__(self):
        ranks = [{"rank":"A", "value":11},
                {"rank":"2", "value":2},
                {"rank":"3", "value":3},
                {"rank":"4", "value":4},
                {"rank":"5", "value":5},
                {"rank":"6", "value":6},
                {"rank":"7", "value":7},
                {"rank":"8", "value":8},
                {"rank":"9", "value":9},
                {"rank":"10", "value":10},
                {"rank":"J", "value":10},
                {"rank":"Q", "value":10},
                {"rank":"K", "value":10}]
        suits = ["spades", "club", "heart", "diamonds"]
        self.cards = []

        for suit in suits:
            for rank in ranks:    
                self.cards.append(Card(suit, rank))
    
    def shuffle(self):
        if len(self.cards) > 1:
            random.shuffle(self.cards)
    
    def deal(self, number):
        card_dealt = []
        for x in range(number):
            if len(self.cards) > 0:
                card = self.cards.pop(0)  
                card_dealt.append(card)
        return card_dealt

class Hand:
    def __init__(self, dealer=False):
        self.cards = []
        self.dealer = dealer
        self.value = 0

    def add_card(self, card_list):
        self.cards.extend(card_list)

    def calculate_values(self):
        self.value = 0
        has_ace = False
        for card in self.cards:
            card_value = int(card.rank["value"])
            self.value += card_value 
            if card.rank["rank"] == "A":
                has_ace = True

        if has_ace and self.value > 21:
            self.value -= 10

    def get_value(self):
        return self.value
    
    def is_blackjack(self):
        return self.get_value() == 21
    
    def display(self, show_all_dealer_cards=False):
        print(f'''{"Dealer's" if self.dealer else "Your"} hand:''')
        for index, card in enumerate(self.cards):
            if index == 0 and self.dealer and not show_all_dealer_cards and not self.is_blackjack():
                print("hidden")
            else:
                print(card)
        if not self.dealer:
            print("Value", self.get_value())

class Game:
    def play(self):
        game_number = 0
        game_to_play = 0
        while game_to_play <= 0:    
            try:
                game_to_play = int(input("How many games do you want to play: "))  
            except:
                print("you must enter a number")
        while game_number < game_to_play:
            game_number += 1

            deck = Deck()    
            deck.shuffle()

            player_hand = Hand()
            dealer_hand = Hand(dealer=True)

            for i in range(2):
                player_hand.add_card(deck.deal(1))
                dealer_hand.add_card(deck.deal(1))

            player_hand.calculate_values()  
            dealer_hand.calculate_values()  
            
            print()
            print("*" * 30)
            print(f"Game {game_number} of {game_to_play}")
            print("*" * 30)
            player_hand.display()
            dealer_hand.display()    

            if self.check_win(player_hand, dealer_hand):
                continue
            choice = ""
            while player_hand.get_value() < 21 and choice not in ['s', 'stand']:
                choice = input("Please choose 'hit' or 'stand': ").lower()
                print()
                while choice not in ['h', 's', 'hit', 'stand']:
                    print(" You should choose one of hit or stand (or h/s)")
                    choice = input("Please choose 'hit' or 'stand': ").lower()
                if choice in ['h', 'hit']:
                    player_hand.add_card(deck.deal(1))
                    player_hand.calculate_values()  
                    player_hand.display()
            if self.check_win(player_hand, dealer_hand):
                continue
            dealer_hand_value = dealer_hand.get_value()
            player_hand_value = player_hand.get_value()

            while dealer_hand_value < 17:
                dealer_hand.add_card(deck.deal(1))
                dealer_hand.calculate_values()  
                dealer_hand_value = dealer_hand.get_value()

            dealer_hand.display(show_all_dealer_cards=True)
            if self.check_win(player_hand, dealer_hand):
                continue
            
            print("final results")
            print("your hand", player_hand_value)
            print("dealer hand", dealer_hand_value)

            self.check_win(player_hand, dealer_hand, True)

        print("\nThanks for playing")

    def check_win(self, player_hand, dealer_hand, game_over=False):
        if not game_over:
            if player_hand.get_value() > 21:
                print("You busted! Dealer wins.")
                return True
            elif dealer_hand.get_value() > 21:
                print("You win!")
                return True
            elif dealer_hand.is_blackjack() and player_hand.is_blackjack():
                print("Tie")
                return True
            elif player_hand.is_blackjack():
                print("You win")
                return True
            elif dealer_hand.is_blackjack():
                print("You lose")
                return True
        else:
            if player_hand.get_value() > dealer_hand.get_value():
                print("you win")

            elif player_hand.get_value() < dealer_hand.get_value():
                print("you lose")
            else:
                print("dealer wins")
            return True
        return False

g = Game()
g.play()


