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

  before_shuffle_deck = deck.copy() 

  for i in range(len(deck)):
    # Generate a random index to swap with
    j = random.randint(0, len(deck) - 1) 
    # Swap the cards at positions i and j
    deck[i], deck[j] = deck[j], deck[i]

  return before_shuffle_deck, deck

# Create and shuffle the deck
my_deck = createDeck()
before_shuffle_deck, shuffled_deck = shuffle(my_deck)

# Print the original and shuffled decks
print("Before Shuffling:", before_shuffle_deck)
print("Shuffled Deck:", shuffled_deck)