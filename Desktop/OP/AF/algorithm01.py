def main(data, points):
    #TODO: modify for no_hurry
    cur = data[0][2:4]
    point = points + abs(data[0][2] - data[0][0]) + abs(data[0][3] - data[0][1])
    time = data[0][4] + abs(data[0][2] - data[0][0]) + abs(data[0][3] - data[0][1])
    del data[0]
    while True:
        search_data = current_data(time, data)
        if search_data == 1:
            return data, point
        n = best_option(search_data[0], cur, time, points)
        time += n[1]
        cur = search_data[0][n[0]][2:4]
        point += n[2]
        del data[n[0] + search_data[1]]
        if n[0] >= len(data) - 5:
            return data, point


def best_option(cur_data, cur, steps, points):
    best_index = 0
    best_len = 0
    end =500
    if len(cur_data)< 500:
        end = len(cur_data)
    for i in range(end):
        if next_coordinate(cur, data[i], steps):
            l = abs(cur_data[i][2] - cur_data[i][0]) + abs(cur_data[i][3] - cur_data[i][1])
            if best_len == 0:
                best_index = i
                best_len = l
            elif l > best_len:
                best_index = i
                best_len = l
    shortest_distance = abs(cur_data[best_index][0] - cur[0]) + abs(cur_data[best_index][1] - cur[1]) + abs(
        cur_data[best_index][2] - cur_data[best_index][0]) + abs(
        cur_data[best_index][3] - cur_data[best_index][1]) + cur_data[best_index][4] - abs(cur_data[best_index][0] - cur[0]) + abs(
        cur_data[best_index][1] - cur[1])
    if next_coordinate1(cur, data[i], steps):
        best_len += points
    return best_index, shortest_distance, best_len


def next_coordinate(cur_position, next_ride, steps):
    # next ride-> [x1, x2, y1, y2, earlieststart, latestfinish)
    if abs(next_ride[0] - cur_position[0]) + abs(next_ride[1] - cur_position[1]) + abs(
        next_ride[1] - next_ride[0]) + abs(next_ride[3] - next_ride[2]) < next_ride[5] - steps:
        return True
    else:
        return False


def next_coordinate1(cur_position, data, steps):
    """Check if we can take next ride"""
    # cur_position and    next ride-> [x1, x2, y1, y2, earlieststart, latestfinish)
    if abs(data[0] - cur_position[0]) + abs(data[1] - cur_position[1]) <= data[4] - steps:
        return 1
    else:
        return 0


def current_data(curr_steps, data):
    """
    Change data set according to time
    """
    # print(curr_steps)
    for i in range(len(data)):
        # print("--------------")
        # print(data[i])
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

total_points = 0
for i in range(cars):
    if len(data) < 1:
        break
    l = main(data, points)
    data = l[0]
    total_points += l[1]

print(len(data))
print(total_points)
