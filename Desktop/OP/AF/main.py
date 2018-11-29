# import pandas as pd
#
# conditions = pd.read_csv("/Users/daradzhala/Desktop/OP/algorithm/AdFontes/qualification_round_2018.in/a_example.in",
#                          sep=" ", nrows=1, header=None,
#                          names=["rows", "columns", "vehicles", "rides", "bonuses", "steps"])
#
# data = pd.read_csv('/Users/daradzhala/Desktop/OP/algorithm/AdFontes/qualification_round_2018.in/a_example.in', sep=" ",
#                    header=None, names=["from_x", "from_y", "to_x", "to_y", "start", "finish"], skiprows=[1])
# print conditions
# print data
#
#
# def algo(x1, y1, x2, y2, lst):
#     pass


class Game:
    def __init__(self, path):
        self.path = path
        with open(self.path) as file:
            data = file.readline()
            data = data.split(" ")
            self.car = int(data[2])
            self.rides = int(data[3])
            self.bonus = int(data[4])
            self.steps = int(data[5].replace("\n", ""))

    def data(self):
        with open(self.path) as file:
            data = file.readlines()
            del data[0]
            data_ = []
            for line in data:
                data_.append([int(x) for x in line.split(" ")])
            data_.sort(key=lambda x: x[4])
            print(data_)


class Car:
    def __init__(self):
        pass

    def starting_point(self, point):
        self.starting_point = point

    def next_ride(self):
        pass


m = Game("/Users/daradzhala/Desktop/OP/AF/qualification_round_2018.in/b_should_be_easy.in")
print(m.data())


def next_coordinate(cur_position, next_ride, time_cur, time_next):
    """Check if we can take next ride"""
    # cur_position and next_ride is lst = [x,y]
    if abs(next_ride[0] - cur_position[0]) + abs(next_ride[1] - cur_position[1]) > time_next - time_cur:
        return False
    else:
        return True


def best_option(cur, data):
    """Check the next 5 rides for the best option to get to the next point and return best option"""
    # cur (current point)-> lst[x, y]
    best = 0
    for i in range(1, 5):
        # length of the distance from current point to start of ride and to the end of the ride
        l = abs(data[i][0] - cur[0]) + abs(data[i][1] - cur[1]) + abs(data[i][2] - data[i][0]) + abs(
            data[i][3] - data[i][1])
        # for the current best option(shortest)
        cur_best = abs(data[best][0] - cur[0]) + abs(data[best][1] - cur[1]) + abs(data[best][2] - data[best][0]) + abs(
            data[best][3] - data[best][1])
        if cur_best > l:
            best = i


