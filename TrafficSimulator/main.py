import random

global_car_count = 0
global_lane_count = 2


def generate_random_cars(car_count, lane_count, min_distance=0, max_distance=20, min_speed=1, max_speed=10):
    global global_car_count
    global global_lane_count
    global_car_count = car_count
    global_lane_count = lane_count
    return [
        (
            random.randint(0, lane_count - 1),
            min_distance + (max_distance - min_distance) * random.random(),
            min_speed + (max_speed - min_speed) * random.random()
        )
        for _ in range(0, car_count)
    ]


def takeDist(elem):
    return elem[0][1]


def update_distance_helper(cars):
    # divide the cars into groups based on its lane
    lanes = [[] for i in range(global_lane_count)]
    for i in range(len(cars)):
        lanes[cars[i][0]].append((cars[i], i))
    for lane in lanes:
        # sort the car from far to close
        lane = sorted(lane, key=takeDist, reverse=True)
        taken_slot = {}
        for car in lane:
            lane_num = car[0][0]
            dist = car[0][1]
            speed = car[0][2]
            if speed < 1 or speed > 10:
                raise Exception('invalid speed')
            curr_loc = dist + speed
            if str(curr_loc) not in taken_slot:
                cars[car[1]] = (lane_num, curr_loc, speed)
                taken_slot[str(curr_loc)] = speed
            else:
                speed = taken_slot[str(curr_loc)]
                cars[car[1]] = (lane_num, curr_loc, speed)
    return cars


def update_distance(cars,elapsed_time):
    for time in range(elapsed_time):
        cars = update_distance_helper(cars)
    return cars

