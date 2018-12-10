def main(data, points):
    cur = data[0][2:4]
    ind = 0
    point = points
    cur_steps = data[0][4] + abs(data[0][2] - data[0][0]) + abs(data[0][3] - data[0][1])
    del data[0]
    while True:
        search_data = current_data(cur_steps, data)
        if search_data == 1:
            return data, point
        n = best_option(cur, search_data[0], cur_steps, ind)
        cur_steps += n[1]
        # print(data[n[0] + search_data[1]])

        ind = n[0]
        cur = search_data[0][n[0]][2:4]
        point += points
        del data[n[0] + search_data[1]]
        if n[0] >= len(data) - 5:
            return data, point


def best_option(cur, data, cur_steps, index_last_ride):
    """Check the next n rides for the best_index option to get to the next point and return best_index option"""
    # cur (current point)-> lst[x, y]
    # data (data set) -> lst[x1, x2, y1,y2, start, finish)
    # cur_steps -> int,
    end = check(cur, data, cur_steps)
    best_index = 0
    best_length = 0
    if index_last_ride == 0:
        index_last_ride = 0
    for i in range(int(index_last_ride), end):
        if next_coordinate(cur, data[i][2:4], cur_steps, data[i][4]):
            # length of the distance from current point to start of ride and to the end of the ride
            l = abs(data[i][0] - cur[0]) + abs(data[i][1] - cur[1]) + abs(data[i][2] - data[i][0]) + abs(
                data[i][3] - data[i][1]) + data[i][4] - abs(data[i][0] - cur[0]) + abs(data[i][1] - cur[1])
            if best_length == 0:
                best_index = i
                best_length = l
            elif best_length > l:
                best_index = i
                best_length = l
    # print(abs(data[best_index][2:4][0] - cur[0]) + abs(data[best_index][1] - cur[1]), data[best_index][4]- cur_steps)
    # print("best idex", best_index)
    # print("best_length", best_length)
    return best_index, best_length


def check(cur, data, cur_steps):
    """Define the borders for optimal search of ride"""
    # cur (current point)-> lst[x, y]
    # data (data set) -> lst[x1, x2, y1,y2, start, finish)

    # lst[length of ride, finish point, number of steps in the end of ride]
    end = False
    lst = []
    for i in range(len(data)):
        if next_coordinate(cur, data[i][2:4], cur_steps, data[i][4]) == 1:
            if lst is False:
                l = abs(data[i][0] - cur[0]) + abs(data[i][1] - cur[1]) + abs(data[i][2] - data[i][0]) + abs(
                    data[i][3] - data[i][1]) + data[4] - abs(data[i][0] - cur[0]) + abs(data[i][1] - cur[1])
                lst.append([l, data[i][2:4], cur_steps + l])
            else:
                for j in range(len(lst)):
                    if next_coordinate(lst[j][1], data[i][2:4], lst[j][2], data[i][4]):
                        end = True
                        return i + 1
                l = abs(data[i][0] - cur[0]) + abs(data[i][1] - cur[1]) + abs(data[i][2] - data[i][0]) + abs(
                    data[i][3] - data[i][1]) + data[i][4] - abs(data[i][0] - cur[0]) + abs(data[i][1] - cur[1])
                lst.append([l, data[i][2:4], cur_steps + l])
    return len(data)


def next_coordinate(cur_position, next_ride, time_cur, time_next):
    """Check if we can take next ride"""
    # cur_position and next_ride is lst = [x,y]
    if abs(next_ride[0] - cur_position[0]) + abs(next_ride[1] - cur_position[1]) <= time_next - time_cur:
        return 1
    else:
        return 0



def current_data(curr_steps, data):
    """
    Change data set according to time
    """
    for i in range(len(data)):
        if data[i][4] > curr_steps:
            return data[i:], i
    return 1


cars = 0
points = 0
with open("/Users/daradzhala/Desktop/OP/AF/qualification_round_2018.in/d_metropolis.in") as file:
    my_line = file.readline()
    my_line = my_line.split(" ")
    cars = int(my_line[2])
    points = int(my_line[4])
    data = file.readlines()
    del data[0]
    data_ = []
    for line in data:
        data_.append([int(x) for x in line.split(" ")])
    data_.sort(key=lambda x: x[4])
    # data -> [518, 656, 201, 494, 186, 712]
    data = data_

print(cars)
total_points = 0
for i in range(cars):
    if len(data) < 1:
        break
    l = main(data, points)
    data = l[0]
    total_points += l[1]

print(len(data))
print(total_points)
