from random import shuffle

class Cards:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
	
    def __str__(self):
        return f"{self.value} of {self.suit}"

class Deck:
    def __init__(self):
        suits = ['clubs','diamonds','hearts','spades']
        values = ['A', '2' , '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        self.cards = []
        
        for s in suits:
            for v in values:
                self.cards.append(Cards(s,v))

    def __str__(self):
        return f"{len(self.cards)} - cards left in the deck"

    def shuffle(self):
        shuffle(self.cards)
        return self

    def deal(self):
        if len(self.cards) == 0:
            raise ValueError("No cards left in the deck")
        return self.cards.pop()


a = Deck()
print(a.deal())
print(a.shuffle())
print(a.deal())
print(a.shuffle())
print(a.deal())
print(a.shuffle())
print(a.deal())
print(a.shuffle())
print(a.deal())
print(a.shuffle())
print(a.deal())
print(a.shuffle())
print(a.deal())
print(a.shuffle())
print(a.deal())
print(a.shuffle())
print(a.deal())
print(a.shuffle())
print(a.deal())
print(a.shuffle())
print(a.deal())
print(a.shuffle())
print(a.deal())
print(a.shuffle())
print(a.deal())
print(a.shuffle())
print(a.deal())
print(a.shuffle())
print(a.deal())
print(a.shuffle())
print(a.deal())
print(a.shuffle())
print(a.deal())
print(a.shuffle())
