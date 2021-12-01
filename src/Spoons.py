import random
import sys
sys.path.append('/home/derek/Documents/UoG/GA1/FPSE/Week3/unitTesing/PairProgramming/PythonOOCardGames')
from src.PlayingCard import PlayingCard

# Game is very simple one called Spoons
# The idea is that each player picks up and discards a card, and plays any hand of 4 matching values
# Each player is dealt 4 cards - Dealer pcks up a card from the pile and chooses a card to discard - which player 2 picks up and chooses a discard etc.
# Dealer keeps drawing cards until the stock pile is exhauseted, and then draws on the discard pile created by the last player
# play ends when one player has 4 of a kind

class Spoons:
    playing_card = PlayingCard()

    def initialiseDeck(self):
        newSpoonsDeck = self.playing_card.generate_deck()
        spoonsDeck = self.playing_card.shuffle_cards(newSpoonsDeck)
        return(spoonsDeck)


    def dealCards(self,spoonsDeck, numberOfPlayers):
        hands = self.playing_card.deal_cards(spoonsDeck,4,numberOfPlayers)
        return(spoonsDeck, hands)


    def playDealerHand(self, stockPile, spoonsHands):

        return(stockPile, spoonsHands)



    def playASpoonsRound(self, stockPile, spoonsHands):
        stockPile, spoonsHands = self.playDealerHand(stockPile, spoonsHands)

        return(stockPile, spoonsHands)




    def play(self):
        numberOfPlayers = 6
        spoonsDeck = self.initialiseDeck()
        # print(spoonsDeck)
        stockPile, spoonsHands = self.dealCards(spoonsDeck, numberOfPlayers)
        # print(stockPile)
        # print(spoonsHands)
        stockPile, spoonsHands = self.playASpoonsRound(stockPile, spoonsHands)



def main():
    spoons = Spoons()
    spoons.play()



if __name__ == "__main__":
    main()