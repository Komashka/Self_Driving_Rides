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
            # print(data_)
            # data -> [518, 656, 201, 494, 186, 712]
            return data_


class Car:
    def __init__(self, data, steps, points):
        self.data = data
        self.steps = 0
        self.max_steps = steps
        self.cur_steps = 0
        self.per_ride = points
        self.points = 0

    def do_ride(self):
        cur = self.data[0][2:4]
        ind = 0
        self.cur_steps += self.data[0][4] + abs(self.data[0][2] - self.data[0][0]) + abs(self.data[0][3] - self.data[0][1])
        del self.data[0]
        while True:
            n = self.best_option(cur, self.data, self.cur_steps, ind)
            self.cur_steps += n[1]
            ind = n[0]
            if self.cur_steps > self.max_steps:
                return self.points, self.steps
            cur = self.data[n[0]][2:4]
            self.points += self.per_ride
            del self.data[n[0]]
            if len(self.data) - 10 < n[0] < len(self.data):
                return self.points, self.steps

    def best_option(self, cur, cur_steps, index_last_ride):
        """Check the next n rides for the best_index option to get to the next point and return best_index option"""
        # cur (current point)-> lst[x, y]
        # data (data set) -> lst[x1, x2, y1,y2, start, finish)
        # cur_steps -> int,
        end = self.check(cur)
        best_index = 0
        best_length = 0
        for i in range(index_last_ride, end):
            if self.next_coordinate(cur, self.data[i][2:4], cur_steps, self.data[i][4]):
                # length of the distance from current point to start of ride and to the end of the ride
                l = abs(self.data[i][0] - cur[0]) + abs(self.data[i][1] - cur[1]) + abs(self.data[i][2] - self.data[i][0]) + abs(
                    self.data[i][3] - self.data[i][1]) + self.data[4] - abs(self.data[i][0] - cur[0]) + abs(self.data[i][1] - cur[1])
                if i == 0:
                    best_index = i
                    best_length = l
                elif best_length < l:
                    best_index = i
                    best_length = l
        return best_index, best_length

    def check(self, cur):
        """Define the borders for optimal search of ride"""
        # cur (current point)-> lst[x, y]
        # data (data set) -> lst[x1, x2, y1,y2, start, finish)

        # lst[length of ride, finish point, number of steps in the end of ride]
        end = False
        lst = []
        for i in range(len(self.data)):
            if self.next_coordinate(cur, self.data[i][2:4], self.cur_steps, self.data[i][4]):
                if lst is False:
                    l = abs(self.data[i][0] - cur[0]) + abs(self.data[i][1] - cur[1]) + abs(self.data[i][2] - self.data[i][0]) + abs(
                        self.data[i][3] - self.data[i][1]) + self.data[4] - abs(self.data[i][0] - cur[0]) + abs(self.data[i][1] - cur[1])
                    lst.append([l, self.data[i][2:4], self.cur_steps + l])
                else:
                    for j in lst:
                        if self.next_coordinate(lst[j][1], self.data[i][2:4], lst[2], self.data[i][4]):
                            end = True
                            return end + 1

                    l = abs(self.data[i][0] - cur[0]) + abs(self.data[i][1] - cur[1]) + abs(self.data[i][2] - self.data[i][0]) + abs(
                        self.data[i][3] - self.data[i][1]) + self.data[4] - abs(self.data[i][0] - cur[0]) + abs(self.data[i][1] - cur[1])
                    lst.append([l, self.data[i][2:4], self.cur_steps + l])

    def next_coordinate(self, cur_position, next_ride, time_cur, time_next):
        """Check if we can take next ride"""
        # cur_position and next_ride is lst = [x,y]
        if abs(next_ride[0] - cur_position[0]) + abs(next_ride[1] - cur_position[1]) > time_next - time_cur:
            return False
        else:
            return True


m = Game("/Users/daradzhala/Desktop/OP/AF/qualification_round_2018.in/b_should_be_easy.in")
print(m.data())
