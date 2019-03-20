from TrafficSimulator.main import update_distance
import unittest


class TrafficSimulator(unittest.TestCase):


        # condition:  1) two cars are on the same lane
        #             2) time goes by 0
        # expect: car1: distance increase by 0; keep speed
        #         car2: distance increase by 0; keep speed
        def test_basic_case0(self):
            cars = [(0, 1, 1), (0, 0, 2)]
            cars = update_distance(cars, elapsed_time=0)
            assert cars == [(0, 1, 1), (0, 0, 2)]

        # condition:  1) two cars are on the same lane
        #             2) time goes by 1
        # expect: car1: distance increase by 1; keep speed
        #         car2: distance increase by 2; speed modifies to the previous car
        def test_basic_case1(self):
            cars = [(0, 1, 1), (0, 0, 2)]
            cars = update_distance(cars, elapsed_time=1)
            assert cars == [(0, 2, 1), (0, 2, 1)]

        # condition:  1) two cars are on the same lane
        #             2) time goes by 2
        # expect: car1: distance increase by 2; keep speed
        #         car2: distance increase by 3; speed modifies to the previous car
        def test_basic_case2(self):
            cars = [(0, 1, 1), (0, 0, 2)]
            cars = update_distance(cars, elapsed_time=2)
            assert cars == [(0, 3, 1), (0, 3, 1)]

        # condition:  1) two cars are on the same lane
        #             2) time goes by 5
        # expect: car1: distance increase by 5; keep speed
        #         car2: distance increase by 6; speed modifies to the previous car
        def test_basic_case3(self):
            cars = [(0, 1, 1), (0, 0, 2)]
            cars = update_distance(cars, elapsed_time=5)
            assert cars == [(0, 6, 1), (0, 6, 1)]

        # condition:  1) two cars are on the same lane
        #             2) time goes by 5
        # expect: car1: distance increase by 5; keep speed
        #         car2: distance increase by 40; keep speed
        def test_basic_case9(self):
            cars = [(0, 1, 1), (0, 5, 8)]
            cars = update_distance(cars, elapsed_time=5)
            assert cars == [(0, 6, 1), (0, 45, 8)]

        # condition: 1) two cars are on different lane
        #            2) time goes by 3
        # expect: car1: distance increase by 15; keep speed
        #         car2: distance increase by 6; keep speed
        def test_basic_case4(self):
            cars = [(0, 0, 5), (1, 0, 2)]
            cars = update_distance(cars, elapsed_time=3)
            assert cars == [(0, 15, 5), (1, 6, 2)]


        # condition: 1) two cars are on different lane
        #            2) time goes by 3
        # expect: car1: distance increase by 3; keep speed
        #         car2: distance increase by 18; keep speed
        def test_basic_case5(self):
            cars = [(0, 1, 1), (1, 0, 6)]
            cars = update_distance(cars, elapsed_time=3)
            assert cars == [(0, 4, 1), (1, 18, 6)]

        # condition: 1) one car stops on the road (speed = 0)
        # expect: an error message
        def test_basic_case6(self):
            cars = [(0, 1, 1), (1, 0, 0)]
            try:
                update_distance(cars, elapsed_time=1)
            except Exception as e:
                assert str(e) == 'invalid speed'

        # condition: 1) one car goes backward on the road (speed < 0)
        # expect: an error message
        def test_basic_case7(self):
            cars = [(0, 1, 1), (1, 0, -2)]
            try:
                update_distance(cars, elapsed_time=7)
            except Exception as e:
                assert str(e) == 'invalid speed'

        # condition: 1) one car is speedy(speed > 10 )
        # expect: an error message
        def test_basic_case8(self):
            cars = [(0, 1, 1), (1, 0, 10)]
            try:
                update_distance(cars, elapsed_time=10)
            except Exception as e:
                assert str(e) == 'invalid speed'


if __name__ == '__main__':
    unittest.main()
