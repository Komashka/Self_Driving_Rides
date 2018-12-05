def do_ride(data, cur_steps, point):
    cur = data[0][2:4]
    ind = 0
    point += 25
    cur_steps += data[0][4] + abs(data[0][2] - data[0][0]) + abs(data[0][3] - data[0][1])
    del data[0]
    while True:
        search_data = current_data(cur_steps, data)
        if search_data == 1:
            return data, cur_steps, point
        n = best_option(cur, search_data[0], cur_steps, ind)
        if n == 1:
            return data, cur_steps, point
        cur_steps += n[1]
        # print(data[n[0] + search_data[1]])

        ind = n[0]
        cur = search_data[0][n[0]][2:4]
        point += 25
        del data[n[0] + search_data[1]]
        if n[0] >= len(data) - 5:
            return data, cur_steps, point


def best_option(cur, data, cur_steps, index_last_ride):
    """Check the next n rides for the best_index option to get to the next point and return best_index option"""
    # cur (current point)-> lst[x, y]
    # data (data set) -> lst[x1, x2, y1,y2, start, finish)
    # cur_steps -> int,
    if index_last_ride == 0:
        index_last_ride = 0
    for i in range(int(index_last_ride), len(data)):
        if next_coordinate(cur, data[i][2:4], cur_steps, data[i][4]):
            # length of the distance from current point to start of ride and to the end of the ride
            l = abs(data[i][0] - cur[0]) + abs(data[i][1] - cur[1]) + abs(data[i][2] - data[i][0]) + abs(
                data[i][3] - data[i][1]) + data[i][4] - abs(data[i][0] - cur[0]) + abs(data[i][1] - cur[1])
            return i, l

    return 1


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


data = []
with open("/Users/daradzhala/Desktop/OP/AF/qualification_round_2018.in/b_should_be_easy.in") as file:
    data = file.readlines()
    del data[0]
    data_ = []
    for line in data:
        data_.append([int(x) for x in line.split(" ")])
    data_.sort(key=lambda x: x[4])
    # print(data_)
    # data -> [518, 656, 201, 494, 186, 712]
    data = data_

# print(data)
lst = []
l = do_ride(data, 0, 0)
points = 0
lst.append(l[0])
points += l[2]
for i in range(100):
    q = do_ride(lst[i], 0, 0)
    lst.append(q[0])
    points += q[2]

print(points)
