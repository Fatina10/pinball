import re
from flask import Flask

app = Flask(__name__)


def grid_size():
    global gridSize
    global grids
    pattern = '[0-5][3-1] [0-5][3-1]'
    gridSize = int(input("Input x and y coordinates for the grid. (For example, 4 8)\n"))
    temp = str(gridSize)
    match = re.search(pattern, temp)
    if not match:
        print("Please choose values between 2 and 51!")
    grids = [[] for _ in range(gridSize)]
    for i in range(0, gridSize):
        grids[i - 1] = [0 for _ in range(gridSize)]
    return grids


def grid():
    for i in range(0, gridSize):
        print(grids[i - 1])


def bumper_input():
    wall_cost = int(input("Enter the cost for hitting a wall: "))
    p = int(input("Enter the number of bumpers: "))
    if p < 0:
        print("Oops! The number of bumpers must be greater than 0!")
        return

    print("Now enter the x position, y position, value and cost for each bumper. (For example, 2 2 1 0)")
    for p in range(0, p):
        print(p + 1, "Bumper")
        bumper_specs = (input(""))
        pattern = '(\d) (\d) (\d) (\d)'
        match = re.search(pattern, bumper_specs)
        if not match:
            print("Oops!You did not match the pattern in the example!")
            break


def balls_specs():
    balls = int(input("Now enter the number of balls: "))
    if balls < 0:
        print("Oops! The number of balls must be greater than 0!")
    elif balls > 0:
        print("Now enter the x position, y position, "
              "direction of movement and lifetime for each ball. (For example, 2 2 1 0)")
        for balls in range(0, balls):
            print(balls + 1, "Ball")
            ball_details = (input(""))
            pattern = '(\d) (\d) [0-3] [1-9][0-9]*'
            match = re.search(pattern, ball_details)
            if not match:
                print("The direction of movement must be a value from 0 to 3 "
                      "AND the lifetime must be positive!")
                break


if __name__ == '__main__':
    grid_size()
    grid()
    bumper_input()
    balls_specs()


