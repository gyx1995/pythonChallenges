from Risk.main import random_outcome
import unittest


class TestRisk(unittest.TestCase):

        # condition: invalid input value for invading_count
        # expect: invading_wins = -1
        def test_invalid_invading(self):
            invading_wins, defending_wins = random_outcome(-2, 1)
            assert invading_wins == -1

        # condition: invalid input value for defending_count
        # expect: defending_wins = -1
        def test_invalid_defending(self):
            invading_wins, defending_wins = random_outcome(2, 0)
            assert defending_wins == -1

        # condition: valid inputs value for defending_count
        # expect: invading_wins is in the range
        def test_valid_invading(self):
            invading_wins, defending_wins = random_outcome(2, 2)
            assert 0 <= invading_wins <= 2

        # condition: valid inputs value for defending_count
        # expect: defending_wins is in range
        def test_valid_defending(self):
            invading_wins, defending_wins = random_outcome(2, 1)
            assert 0 <= defending_wins <= 1

        # condition: max valid inputs value for both invading_count and defending_count
        # expect: invading_wins and defending_wins are in range
        def test_maxinvading_maxDefending(self):
            invading_wins, defending_wins = random_outcome(3, 3)
            assert 0 <= defending_wins <= 3 and 0 <= defending_wins <= 3


if __name__ == '__main__':
    unittest.main()
