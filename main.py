import re
import time
from flask import Flask

app = Flask(__name__)


def separate_grid_inputs(set):
    x, y = (set.split(' '))
    return int(x), int(y)


def grid_size():
    global gridSize
    global grids
    pattern = '(\d) (\d)'
    gridSize = input("Input x and y coordinates for the grid. (For example, 4 8)\n")
    match = re.match(pattern, gridSize)
    if not match:
        print("Please choose values between 2 and 51!")
    x, y = separate_grid_inputs(gridSize)
    grids = [[] for _ in range(x)]
    for i in range(0, x):
        grids[i] = [0 for _ in range(y)]
    for i in grids:
        print(i)
    return grids


def separate_bumper_inputs(set):
    x, y, val, cost = (set.split(' '))
    return int(x), int(y), int(val), int(cost)


def bumper_input():
    global wall_cost
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
        x, y, val, cost = separate_bumper_inputs(bumper_specs)
        grids[x - 1][y - 1] = 1
        for item in grids:
            print(item)
        if not match:
            print("Oops!You did not match the pattern in the example!")
            break


def separate_ball_inputs(set):
    x_b, y_b, dom, lt = (set.split(' '))
    return int(x_b), int(y_b), int(dom), int(lt)


def is_wall(x, y, grid_y):
    if x == 1 or y == grid_y:
        return True


def rebound_direction(dom):
    if dom == 0:
        return 3

    elif dom == 1:
        return 0

    elif dom == 2:
        return 1

    elif dom == 3:
        return 2


def move_right(lt, x_b, y_b, grid_y):
    while lt > 0:
        if is_wall(x_b, y_b, grid_y) and lt >= 1:
            lt = lt - wall_cost
            dom = rebound_direction(0)
            time.sleep(2)
            print("Rebounding...")
            for n in grids:
                print(n)
            return lt, dom, x_b, y_b
        print("Moving Right...")
        time.sleep(1)
        print("x = ", x_b)
        print("y = ", y_b)
        grids[x_b - 1][y_b - 1] = 0
        grids[x_b - 1][y_b] = 'b'
        y_b = y_b + 1
        lt = lt - 1
        print("Lifetime ", lt)
        for n in grids:
            print(n)
    return lt, 0, x_b, y_b


def move_up(lt, x_b, y_b, grid_y):
    while lt > 0:
        print("x =", x_b)
        print("y =", y_b)
        if is_wall(x_b, y_b, grid_y) and lt >= 1:
            lt = lt - wall_cost
            dom = rebound_direction(1)
            time.sleep(2)
            print("Rebounding...")
            for n in grids:
                print(n)
            return lt, dom, x_b, y_b
        print("Moving up...")
        time.sleep(1)
        grids[x_b - 1][y_b - 1] = 0
        grids[x_b - 2][y_b - 1] = 'b'
        x_b = x_b - 1
        lt = lt - 1
        for n in grids:
            print(n)
    return lt, 1, x_b, y_b


def move_left(lt, x_b, y_b, grid_y):
    while lt > 0 and y_b < grid_y:
        if is_wall(x_b, y_b, grid_y) and lt >= 1:
            lt = lt - wall_cost
            dom = rebound_direction(2)
            time.sleep(2)
            print("Rebounding...")
            for n in grids:
                print(n)
            return lt, dom, x_b, y_b
        print("Moving left...")
        time.sleep(1)
        grids[x_b - 1][y_b - 1] = 0
        grids[x_b - 1][y_b - 2] = 'b'
        y_b = y_b - 1
        lt = lt - 1
        for n in grids:
            print(n)
    return lt, 2, x_b, y_b


def move_down(lt, x_b, y_b, grid_y):
    while lt > 0:
        if is_wall(x_b, y_b, grid_y) and lt >= 1:
            lt = lt - wall_cost
            dom = rebound_direction(3)
            time.sleep(2)
            print("Rebounding...")
            for n in grids:
                print(n)
            return lt, dom, x_b, y_b
        print("Moving down...")
        time.sleep(1)
        grids[x_b - 1][y_b - 1] = 0
        grids[x_b][y_b - 1] = 'b'
        x_b = x_b + 1
        lt = lt - 1
        for n in grids:
            print(n)
    return lt, 3, x_b, y_b


def balls_specs():
    split_grid_size = gridSize.split()
    grid_x = int(split_grid_size[0])
    grid_y = int(split_grid_size[1])
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
            x_b, y_b, dom, lt = separate_ball_inputs(ball_details)
            grids[x_b - 1][y_b - 1] = 'b'
            print("Initial position of ball represented as 'b':")
            for d in grids:
                print(d)
            time.sleep(1)
            # pass
            while lt > 0:
                if dom == 0:
                    lt, dom, x_b, y_b = move_right(lt, x_b, y_b, grid_y)

                elif dom == 1:
                    lt, dom, x_b, y_b  = move_up(lt, x_b, y_b, grid_y)

                elif dom == 2:
                    lt, dom, x_b, y_b = move_left(lt, x_b, y_b, grid_y)

                elif dom == 3:
                    lt, dom, x_b, y_b  = move_down(lt, x_b, y_b, grid_y)

                else:
                    print("Invalid direction of movement! "
                          "Please choose values between 0 to 3")


if __name__ == '__main__':
    grid_size()
    bumper_input()
    balls_specs()
