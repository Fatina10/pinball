from main import main
class Balls:
    def balls_specs(self):
        balls = int(input("Now enter the number of balls: "))
        if balls < 0:
            print("Oops! The number of balls must be greater than 0!")
        elif balls > 0:
            print("Now enter the x position, y position, "
                  "direction of movement and lifetime for each ball. (For example, 2 2 1 0)")
            for balls in range(0, balls):
                print(balls + 1, "Ball")
                balls_specs = (input(""))
                pattern = '(\d) (\d) [0-3] [1-9][0-9]*'
                match = re.search(pattern, balls_specs)
                if not match:
                    print("The direction of movement must be a value from 0 to 3 "
                          "AND the lifetime must be positive!")
                    break
