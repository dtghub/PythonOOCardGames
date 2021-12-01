import unittest
import sys
sys.path.append('/home/derek/Documents/UoG/GA1/FPSE/Week3/unitTesing/PairProgramming/PythonOOCardGames')
from src.Spoons import Spoons



class SpoonsTest(unittest.TestCase):
    spoons = Spoons
    def test_test(self):
        self.assertEqual(True, True)


    def  test_initialiseDeck(self):
        result = self.spoons.initialiseDeck(self)
        self.assertEqual(52, len(result))


if __name__ == "__main__":
    unittest.main()
