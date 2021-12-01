import random
import sys
sys.path.append('/home/derek/Documents/UoG/GA1/FPSE/Week3/unitTesing/cloned/PythonGames')
from src.PlayingCard import *

# Game is very simple one called Spoons
# The idea is that each player picks up and discards a card, and plays any hand of 4 matching values
# Each player is dealt 4 cards - Dealer pcks up a card from the pile and chooses a card to discard - which player 2 picks up and chooses a discard etc.
# Dealer keeps drawing cards until the pstock pile is exhauseted, and then draws on the discard pile created by the last player
# play ends when one player has 4 of a kind




def initialiseDeck():
    newSpoonsDeck = generate_deck()
    spoonsDeck = shuffle_cards(newSpoonsDeck)
    return(spoonsDeck)


def dealCards(spoonsDeck, numberOfPlayers):
    hands = deal_cards(spoonsDeck,4,numberOfPlayers)
    return(spoonsDeck, hands)


def playDealerHand(stockPile, spoonsHands):

    return(stockPile, spoonsHands)



def playASpoonsRound(stockPile, spoonsHands):
    stockPile, spoonsHands = playDealerHand(stockPile, spoonsHands)

    return(stockPile, spoonsHands)




def main():
    numberOfPlayers = 6
    spoonsDeck = initialiseDeck()
    # print(spoonsDeck)
    stockPile, spoonsHands = dealCards(spoonsDeck, numberOfPlayers)
    # print(stockPile)
    # print(spoonsHands)
    stockPile, spoonsHands = playASpoonsRound(stockPile, spoonsHands)


    
main()
