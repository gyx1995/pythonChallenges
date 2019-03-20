import random


def random_outcome(invading_count, defending_count):
    if invading_count < 1 or invading_count > 3 or defending_count < 1 or defending_count > 3:
        return -1,-1
    invading_wins = 0
    defending_wins = 0
    invading_list = sorted(random.sample(range(1, 7), invading_count), reverse=True)
    defending_list = sorted(random.sample(range(1, 7), defending_count), reverse=True)
    for i in range(min(invading_count, defending_count)):
        invade = invading_list[i]
        defend = defending_list[i]
        if invade > defend:
            invading_wins += 1
        else:
            defending_wins += 1
    return invading_wins, defending_wins


def gen_possibilities():
    number_interation = 1000
    for i in range(1,4):
        for d in range(1,4):
            count = 0
            for number in range(number_interation):
                invading_wins = random_outcome(i,d)[0]
                if invading_wins >= 1:
                    count += 1
            perc = count * 100 / number_interation
            s = "with {} invader and {} defender, the probably of the invader winning at least one is about {} %"
            print(s.format(i, d, perc))
