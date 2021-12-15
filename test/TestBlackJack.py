from src.BlackJack import BlackJack
from src.TestInput import TestInput
import unittest

class TestBlackJack(unittest.TestCase):

    black_jack = BlackJack()
    test_input = TestInput()

    def setUp(self):
        self.black_jack.setGameInput(self.test_input)

    def test_black_jack(self):
        self.test_input.set_list_of_test_inputs([3,"T","S"])
        self.black_jack.main()

    def test_valid_deal_input(self):
        self.test_input.set_list_of_test_inputs(["T","S"])
        self.assertEqual("T",self.black_jack.valid_deal_input())


