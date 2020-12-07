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


bumper_list = []


def bumper_input():
    global wall_cost
    global score
    score = 0
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
            return
        bumper_list.append(bumper_specs)
        print("bumper list", bumper_list)
        x, y, val, cost = separate_bumper_inputs(bumper_specs)
        grids[x - 1][y - 1] = p + 1
        for item in grids:
            print(item)


def if_bumper(grid_val, lt, dir):
    x, y, val, cost = separate_bumper_inputs(bumper_list[grid_val-1])
    lt = lt - cost
    dom = rebound_direction(dir)
    time.sleep(1)
    return lt, dom, x, y


def separate_ball_inputs(set):
    x_b, y_b, dom, lt = (set.split(' '))
    return int(x_b), int(y_b), int(dom), int(lt)


def is_wall(x, y, grid_x, grid_y, dom):
    if x == 1 and dom == 1:
        return True
    elif y == grid_y and dom == 0:
        return True
    elif x == grid_x and dom == 3:
        return True
    elif y == 1 and dom == 2:
        return True
    else:
        return False


def rebound_direction(dom):
    if dom == 0:
        return 3

    elif dom == 1:
        return 0

    elif dom == 2:
        return 1

    elif dom == 3:
        return 2


def move_right(lt, x_b, y_b, grid_x, grid_y, temp):
    while lt != 1:
        #check for wall
        if is_wall(x_b, y_b, grid_x, grid_y, 0) and lt >= 1:
            lt = lt - wall_cost
            dom = rebound_direction(0)
            time.sleep(1)
            print("Rebounding...")
            for n in grids:
                print(n)
            return lt, dom, x_b, y_b, temp
        ###edit###
        time.sleep(1)
        # Check for bumper
        if temp == 0:
            print("Moving right...")
            grids[x_b - 1][y_b - 1] = 0
            temp = grids[x_b -1 ][y_b]
            grids[x_b -1][y_b] = 'b'
            y_b = y_b + 1
            lt = lt - 1
            for n in grids:
                print(n)
        else:
            # bumper exists so rebound the ball 90 degrees
            lt, dom, x_b, y_b = if_bumper(int(temp), lt, 0)
            print("Current points")
            print(x_b)
            print(y_b)
            grids[x_b - 1][y_b - 1] = temp
            print("p_temp", temp)
            temp = grids[x_b][y_b - 1]
            print("n_temp", temp)
            grids[x_b][y_b - 1] = 'b'
            x_b = x_b + 1
            for n in grids:
                print(n)
            return lt, dom, x_b, y_b, temp
    return lt, 0, x_b, y_b, temp


def move_up(lt, x_b, y_b, grid_x, grid_y, temp):
    while lt != 1:
        #check for wall
        if is_wall(x_b, y_b, grid_x, grid_y, 1) and lt >= 1:
            lt = lt - wall_cost
            dom = rebound_direction(1)
            time.sleep(1)
            print("Rebounding...")
            for n in grids:
                print(n)
            return lt, dom, x_b, y_b, temp
        # for n in grids:
        #     print(n)
        time.sleep(1)
        # Check for bumper
        if temp == 0:
            print("Moving up...")
            grids[x_b - 1][y_b - 1] = 0
            temp = grids[x_b - 2][y_b - 1]
            grids[x_b - 2][y_b - 1] = 'b'
            x_b = x_b - 1
            lt = lt - 1
            for n in grids:
                print(n)
        else:
            # bumper exists so rebound ball 90 degrees
            print("Rebounding")
            lt, dom, x_b, y_b = if_bumper(int(temp), lt, 1)
            #set ball to the new location after rebound
            grids[x_b - 1][y_b - 1] = temp
            temp = grids[x_b - 1][y_b]
            grids[x_b - 1][y_b] = 'b'
            y_b = y_b + 1
            for n in grids:
                print(n)
            return lt, dom, x_b, y_b, temp
    return lt, 1, x_b, y_b, temp


def move_left(lt, x_b, y_b, grid_x, grid_y, temp):
    while lt != 1:
        # check for wall
        if is_wall(x_b, y_b, grid_x, grid_y, 2) and lt >= 1:
            lt = lt - wall_cost
            dom = rebound_direction(2)
            time.sleep(2)
            print("Rebounding...")
            for n in grids:
                print(n)
            return lt, dom, x_b, y_b, temp
        print("Moving left...")
        time.sleep(1)
        # Check for bumper

        if temp == 0:
            grids[x_b - 1][y_b - 1] = 0
            temp = grids[x_b - 1][y_b - 2]
            grids[x_b - 1][y_b - 2] = 'b'
            y_b = y_b - 1
            lt = lt - 1
            for n in grids:
                print(n)
        else:
            # bumper exists so rebound ball 90 degrees
            lt, dom, x_b, y_b = if_bumper(int(temp), lt, 2)
            # set ball to the new location after rebound
            grids[x_b - 1][y_b - 1] = temp
            temp = grids[x_b - 2][y_b - 1]
            grids[x_b - 2][y_b - 1] = 'b'
            x_b = x_b - 1
            for n in grids:
                print(n)
            return lt, dom, x_b, y_b, temp
    return lt, 2, x_b, y_b, temp


def move_down(lt, x_b, y_b, grid_x,  grid_y, temp):
    while lt != 1:
        #check for wall
        if is_wall(x_b, y_b, grid_x, grid_y, 3) and lt >= 1:
            lt = lt - wall_cost
            dom = rebound_direction(3)
            time.sleep(2)
            print("Rebounding...")
            for n in grids:
                print(n)
            return lt, dom, x_b, y_b, temp
        print("Moving down...")
        time.sleep(1)
        # Check for bumper
        if temp == 0:
            print("temp is zero: ", temp)
            grids[x_b - 1][y_b - 1] = 0
            temp = grids[x_b][y_b - 1]
            grids[x_b][y_b - 1] = 'b'
            x_b = x_b + 1
            lt = lt - 1
            for n in grids:
                print(n)
        else:
            #bumper exists so rebound ball 90 degrees
            lt, dom, x_b, y_b = if_bumper(int(temp), lt, 3)
            #set ball to the new location after rebound
            grids[x_b - 1][y_b - 1] = temp
            temp = grids[x_b - 1][y_b - 2]
            grids[x_b - 1][y_b - 2] = 'b'
            y_b = y_b - 1
            for n in grids:
                print(n)
            return lt, dom, x_b, y_b, temp
    return lt, 3, x_b, y_b, temp


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
            temp = 0
            while lt > 1:
                if dom == 0:
                    lt, dom, x_b, y_b, temp = move_right(lt, x_b, y_b, grid_x,grid_y, temp)

                elif dom == 1:
                    lt, dom, x_b, y_b, temp = move_up(lt, x_b, y_b, grid_x, grid_y, temp)

                elif dom == 2:
                    lt, dom, x_b, y_b, temp = move_left(lt, x_b, y_b, grid_x, grid_y, temp)

                elif dom == 3:
                    lt, dom, x_b, y_b, temp = move_down(lt, x_b, y_b, grid_x, grid_y, temp)

                else:
                    print("Invalid direction of movement! "
                          "Please choose values between 0 to 3")


if __name__ == '__main__':
    grid_size()
    bumper_input()
    balls_specs()