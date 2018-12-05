def main(data):
    cur = data[0][2:4]
    point = 25
    cur_steps = data[0][4] + abs(data[0][2] - data[0][0]) + abs(data[0][3] - data[0][1])
    del data[0]
    while True:
        cur_data = current_data(cur_steps, data)
        if cur_data == 1:
            return data, cur_steps, point
        n = shortest(cur_data[0], cur, cur_steps)
        if n[0] == 0 and n[1] == 0:
            return data, cur_steps, point
        cur_steps += n[1]
        # print(data[n[0] + search_data[1]])
        cur = cur_data[0][n[0]][2:4]
        point += 25
        del data[n[0] + cur_data[1]]
        if n[0] >= len(data) - 5:
            return data, cur_steps, point


def shortest(cur_data, cur, steps):
    short = 0
    short_len = 0
    end = 20
    if len(cur_data) < 20:
        end = len(cur_data)
    for i in range(end):
        if next_coordinate(cur, cur_data[i][2:4], steps, cur_data[i][4]):
            l = abs(cur_data[i][0] - cur[0]) + abs(cur_data[i][1] - cur[1])
            if short == 0:
                short = i
                short_len = l
            elif l < short_len:
                short = i
                short_len = l
    shortest_distance = abs(cur_data[short][0] - cur[0]) + abs(cur_data[short][1] - cur[1]) + abs(
                cur_data[short][2] - cur_data[short][0]) + abs(
                cur_data[short][3] - cur_data[short][1]) + cur_data[short][4] - abs(cur_data[short][0] - cur[0]) + abs(
                cur_data[short][1] - cur[1])
    return short, shortest_distance


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


with open("/Users/daradzhala/Desktop/OP/AF/qualification_round_2018.in/b_should_be_easy.in") as file:
    data = file.readlines()
    del data[0]
    data_ = []
    for line in data:
        data_.append([int(x) for x in line.split(" ")])
    data_.sort(key=lambda x: x[4])
    # data -> [518, 656, 201, 494, 186, 712]
    data = data_

main(data)

lst = []
l = main(data)
points = 0
lst.append(l[0])
points += l[2]
for i in range(100):
    q = main(lst[i])
    lst.append(q[0])
    points += q[2]

print(points)