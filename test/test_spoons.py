import unittest
import sys
sys.path.append('/home/derek/Documents/UoG/GA1/FPSE/Week3/unitTesing/PairProgramming/PythonOOCardGames')
from src.Spoons import Spoons

# we only need this next line because we directly call PlayingCard in test_initialiseDeck_shuffled
from src.PlayingCard import PlayingCard



class SpoonsTest(unittest.TestCase):
    spoons = Spoons()
    playing_card = PlayingCard()
    def test_test(self):
        self.spoons.assertEqual(True, True)


    def  test_initialiseDeck_size(self):
        result = self.spoons.initialiseDeck()
        self.assertEqual(52, len(result))

    def test_initialiseDeck_shuffled(self):
        unshuffled_deck = self.playing_card.generate_deck()
        # initDeckOutput = self.playing_card.generate_deck()
        initDeckOutput = self.spoons.initialiseDeck()
        self.assertNotEqual(unshuffled_deck, initDeckOutput)



def main():
    unittest.main()


if __name__ == "__main__":
    unittest.main()
