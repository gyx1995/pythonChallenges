from CrossWord.main import solve_crossword
import unittest


class TestCrossword(unittest.TestCase):
        ACROSS = 0
        DOWN = 1

        # condition: too many words to fit in the blanks
        # expect: soln == None
        def test_basic_case0(self):
            soln = solve_crossword(vocab=['the', 'begin','ok'],
                                   blanks=[(0, 1, self.ACROSS, 3),
                                           (2, 0, self.DOWN, 5)])
            assert soln is None

        # condition:  valid case - words have more no intersections
        # expect: return a valid solution
        def test_basic_case1(self):
            soln = solve_crossword(vocab=['time', 'electric'],
                                   blanks=[(0, 0, self.ACROSS, 4),
                                           (1, 3, self.ACROSS, 8)])
            assert soln == [(0, 0, self.ACROSS, 'time'),
                           (1, 3, self.ACROSS, 'electric')]

        # condition: valid case - words have one intersection
        # expect:return a valid solution
        def test_basic_case2(self):
            soln = solve_crossword(vocab=['the', 'begin'],
                                   blanks=[(0, 1, self.ACROSS, 3),
                                           (2, 0, self.DOWN, 5)])
            assert soln == [(0, 1, self.ACROSS, 'the'),(2, 0,  self.DOWN, 'begin')]

        # condition:  valid case - words have more than one intersections
        # expect: return a valid solution
        def test_basic_case3(self):
            soln = solve_crossword(vocab=['next', 'time', 'expect', 'electric'],
                                   blanks=[(0, 0, self.ACROSS, 4),
                                           (1, 0, self. DOWN, 6),
                                           (3, 0, self.DOWN, 4),
                                           (1, 3, self.ACROSS, 8)])
            assert soln == [(0, 0, self.ACROSS, 'next'),
                            (3, 0, self.DOWN, 'time'),
                           (1, 0,  self.DOWN, 'expect'),
                           (1, 3, self.ACROSS, 'electric')]

        # condition:  valid case - with too many blanks
        # expect: return a valid solution
        def test_basic_case4(self):
            soln = solve_crossword(vocab=['time', 'next'],
                                   blanks=[(0, 0, self.ACROSS, 4),
                                           (1, 0, self. DOWN, 6),
                                           (3, 0, self.DOWN, 4),
                                           (1, 3, self.ACROSS, 8)])
            assert soln == [(0, 0, self.ACROSS, 'next'), (3, 0, self.DOWN, 'time')]

        # condition:  edge case - one word to fit in
        # expect: return a valid solution
        def test_basic_case5(self):
            soln = solve_crossword(vocab=['time'],
                                   blanks=[(0, 0, self.ACROSS, 4),
                                           (1, 0, self. DOWN, 6),
                                           (3, 0, self.DOWN, 4),
                                           (1, 3, self.ACROSS, 8)])
            assert soln == [(0, 0, self.ACROSS, 'time')]


        # condition:  edge case - no word to fit in
        # expect: return None
        def test_basic_case6(self):
            soln = solve_crossword(vocab=[],
                                   blanks=[(0, 0, self.ACROSS, 4),
                                           (1, 0, self. DOWN, 6),
                                           (3, 0, self.DOWN, 4),
                                           (1, 3, self.ACROSS, 8)])
            assert soln is None

        # condition:  valid inputs but no way to fit in
        # expect: return None
        def test_basic_case6(self):
            soln = solve_crossword(vocab=['next', 'qimed', 'expectd', 'electric'],
                                   blanks=[(0, 0, self.ACROSS, 4),
                                           (1, 0, self. DOWN, 7),
                                           (3, 0, self.DOWN, 5),
                                           (1, 3, self.ACROSS, 8)])
            assert soln is None


if __name__ == '__main__':
    unittest.main()
