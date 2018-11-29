import numpy as np
import pylab as pl
from matplotlib import collections as mc
import matplotlib.pyplot as plt
from math import hypot

# lines of rides
with open("/Users/daradzhala/Desktop/OP/AF/qualification_round_2018.in/b_should_be_easy.in") as file:
    data = file.readlines()
    lines = []
    for i in range(1, len(data)):
        my_line = data[i].split(' ')
        lines.append([(int(my_line[0]), int(my_line[1])), (int(my_line[2]), int(my_line[3]))])

    lc = mc.LineCollection(lines, colors=(1, 0, 0, 1), linewidths=0.5)
    fig, ax = pl.subplots()
    ax.add_collection(lc)
    ax.autoscale()
    ax.margins(0.1)
    plt.show()

# # Dots of beginning and end of the drive
# with open("/Users/daradzhala/Desktop/OP/AF/qualification_round_2018.in/c_no_hurry.in") as file:
#     data = file.readlines()
#     fig, ax = plt.subplots()
#     green_z = [[],[]]
#     blue_z = [[],[]]
#     red_z = [[],[]]
#     for i in range(1, len(data)):
#         my_line = data[i].split(' ')
#         if hypot(int(my_line[2])-int(my_line[0]), int(my_line[3])-int(my_line[1])) < 500:
#             green_z[0].append(int(my_line[0]))
#             green_z[1].append(int(my_line[1]))
#         elif hypot(int(my_line[2])-int(my_line[0]), int(my_line[3])-int(my_line[1])) < 1100:
#             blue_z[0].append(int(my_line[0]))
#             blue_z[1].append(int(my_line[1]))
#         elif hypot(int(my_line[2])-int(my_line[0]), int(my_line[3])-int(my_line[1])) > 1100:
#             red_z[0].append(int(my_line[0]))
#             red_z[1].append(int(my_line[1]))
#
#     ax.scatter(green_z[0], green_z[1], s=1, color='g')
#     ax.scatter(blue_z[0], blue_z[1], s=1, color='b')
#     ax.scatter(red_z[0], red_z[1], s=1, color='r')
#     ax.plot()
#     ax.autoscale()
#     plt.show()




