import copy


def main(data, bonus):
    time, cur_pos, points, solution = 0, [0, 0], 0, []
    while True:
        q = find(data, time, cur_pos, points, solution, bonus)
        if q == 0:
            return solution, points, data
        data, time, cur_pos, points, solution = q
        if data == []:
            return solution, points, data


def find(data, time, cur_pos, points, solution, bonus):
    for ride in data:
        if in_time(ride, time, cur_pos):
            cur_pos = [ride[2], ride[3]]
            delay = ride[4] - time
            if has_bonus(ride,time,cur_pos):
                points += bonus
            time += delay + distance(cur_pos[0], ride[0], cur_pos[1], ride[1]) + distance(ride[0], ride[1], ride[2],
                                                                                          ride[3])
            points += distance(ride[0], ride[1], ride[2], ride[3])
            solution.append(ride)
            data = update_time(data, time)
            return data, time, cur_pos, points, solution
    if len(data)>=1:
        ride = data[0]
        cur_pos = [ride[2], ride[3]]
        delay = ride[4] - time
        # print("delay", delay)
        if has_bonus(ride, time, cur_pos):
            points += bonus
            if delay > 0:
                pass
        time += delay + distance(cur_pos[0], ride[0], cur_pos[1], ride[1]) + distance(ride[0], ride[1], ride[2],
                                                                                      ride[3])
        points += distance(ride[0], ride[1], ride[2], ride[3])
        solution.append(ride)
        data = update_time(data, time)
        return data, time, cur_pos, points, solution


    return 0


def distance(x1, x2, y1, y2):
    return abs(x1 - x2) + abs(y1 - y2)


def in_time(ride, time, cur_pos):
    # cur_pos -> [x,y]

    if (
            distance(cur_pos[0], ride[0], cur_pos[1], ride[1]) + distance(ride[0], ride[1], ride[2], ride[3]) < ride[
        5] - time):
        return True
    return False

def has_bonus(ride, time, cur_pos):
    if distance(cur_pos[0], ride[0], cur_pos[1], ride[1]) + time < ride[4]:
        return True
    return False


def update_time(data, cur):
    for i in range(len(data)):
        if data[i][4] > cur:
            return data[i:]
    return []


cars = 0
bonus = 0
with open("/Users/daradzhala/Desktop/OP/AF/qualification_round_2018.in/b_should_be_easy.in") as file:
    my_line = file.readline()
    my_line = my_line.split(" ")
    cars = int(my_line[2])
    bonus = int(my_line[4])
    data = file.readlines()
    data_ = []
    for line in data:
        data_.append([int(x) for x in line.split(" ")])
    data_.sort(key=lambda x: x[4])
    # data -> [518, 656, 201, 494, 186, 712]
    data = data_

main_data = copy.deepcopy(data)
# print(points)

with open("output.txt", 'w') as file:
    points = 0
    for i in range(cars):
        print("car", i)
        s = main(data , bonus)
        points += s[1]
        cur_sol = s[0]
        output_sol = []
        for ride in cur_sol:
            output_sol.append(str(main_data.index(ride)))
        output_str = " ".join(output_sol)
        output_str = str(i+1) + " " + output_str +"\n"
        file.write(output_str)
        for j in cur_sol:
            # print(j)
            data.remove(j)

    print("total points", points)
