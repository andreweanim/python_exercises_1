import random

# deck of 52 playing cards
def createDeck():

  suits = ['s', 'h', 'd', 'c']
  values = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
  deck = []

  for suit in suits:
    for value in values:
      deck.append(value + suit) 

  return deck

# Card shuffles
def shuffle(deck):
  
  for i in range(len(deck)):
    # Generate a random index to swap with
    j = random.randint(0, len(deck) - 1) 
    # Swap the cards at positions i and j
    deck[i], deck[j] = deck[j], deck[i]

  return deck

def deal(deck, hands, cards_per_hand):
  
  dealt_hands = []
  for _ in range(hands):
    hand = []
    for _ in range(cards_per_hand):
      if len(deck) == 0:
        break
      hand.append(deck.pop(0))
    dealt_hands.append(hand)

  return dealt_hands

# create, shuffled, and deal cards.
class Cards:
  
  def __init__(self):
    self.cards = []

# create cards
  def create(self):
   
    self.cards = createDeck()

# shuffle cards
  def shuffle(self):
    
    self.cards = shuffle(self.cards)

# deal cards
  def deal(self, hands, cards_per_hand):
    
    dealt_hands = deal(self.cards, hands, cards_per_hand)
    return dealt_hands

card_game = Cards()
card_game.create()
card_game.shuffle()

num_hands = int(input("Enter the number of hands: "))
cards_per_hand = int(input("Enter the number of cards per hand: "))

dealt_hands = card_game.deal(num_hands, cards_per_hand)

print("Dealt hands:")
for i, hand in enumerate(dealt_hands):
  print(f"Hand {i+1}: {hand}")