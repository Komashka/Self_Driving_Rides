def do_ride(data, max_steps, cur_steps, point):
    cur = data[0][2:4]
    ind = 0
    point += 25
    cur_steps += data[0][4] + abs(data[0][2] - data[0][0]) + abs(data[0][3] - data[0][1])
    del data[0]
    while True:
        n = best_option(cur, data, cur_steps, ind)
        cur_steps += n[1]
        ind = n[0]
        if cur_steps > max_steps:
            return "finish", point, cur_steps
        cur = data[n[0]][2:4]
        point += 25
        del data[n[0]]
        if len(data) - 3 < n[0] < len(data):
            return 'finish', point, cur_steps, data


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
            if i == 0:
                best_index = i
                best_length = l
            elif best_length > l:
                best_index = i
                best_length = l
    return best_index, best_length


def check(cur, data, cur_steps):
    """Define the borders for optimal search of ride"""
    # cur (current point)-> lst[x, y]
    # data (data set) -> lst[x1, x2, y1,y2, start, finish)

    # lst[length of ride, finish point, number of steps in the end of ride]
    end = False
    lst = []
    for i in range(len(data)):
        if next_coordinate(cur, data[i][2:4], cur_steps, data[i][4]):
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
        return False
    else:
        return True



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
l = do_ride(data, 25000, 0, 0)
print(l)
