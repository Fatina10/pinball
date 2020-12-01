# import re
# from flask import Flask
#
#
# app = Flask(__name__)
#
#
# def separate_grid_inputs(set):
#     x, y = (set.split(' '))
#     return int(x), int(y)
#
# def grid_size():
#     global gridSize
#     global grids
#     pattern = '(\d) (\d)'
#     gridSize = input("Input x and y coordinates for the grid. (For example, 4 8)\n")
#     match = re.match(pattern, gridSize)
#     if not match:
#         print("Please choose values between 2 and 51!")
#     x, y = separate_grid_inputs(gridSize)
#     grids = [[] for _ in range(x)]
#     for i in range(0, x):
#         grids[i - 1] = [0 for _ in range(y)]
#     for i in range(0, x):
#         print(grids[i - 1])
#     return grids
#
# if __name__ == '__main':
def grid_size():
    grids = [[] for _ in range(3)]
    for i in range(0, 3):
        grids[i - 1] = [0 for _ in range(4)]
    for i in range(0, 3):
        print(grids[i - 1])
    return grids


grid_size()