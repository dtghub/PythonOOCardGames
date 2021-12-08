from src.BlackJack import BlackJack
from src.TestInput import TestInput
import unittest

class TestBlackJacl(unittest.TestCase):

    def test_black_jack(self):
        black_jack = BlackJack()
        test_input = TestInput()
        test_input.set_list_of_test_inputs([3,"D","S"])
        black_jack.setGameInput(test_input)
        black_jack.main()


