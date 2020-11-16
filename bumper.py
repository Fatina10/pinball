class Bumper:
    def bumper_input(self):
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