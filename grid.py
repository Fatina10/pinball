class grid:
    def __init__(self, x, y):
        self.m = x
        self.n = y
    def gridSize_def(self):
        global gridSize
        global grids
        while True:
            try:
                grid_pattern = '[0-9999] [0-9999]'
                gridSize = int(input("input grid length and width\n"))
                match = re.search(grid_pattern, gridSize)
                if gridSize < 2 or gridSize > 51:
                    print("invalid int")
                elif not match:
                    print("You did not match the example pattern")
                return
            except ValueError:
                print("invalid input")
                break
        grids = [[] for _ in range(gridSize)]
        for i in range(0, gridSize):
            grids[i - 1] = [0 for _ in range(gridSize)]
        return grids

    def grid_def(self):
        for i in range(0, gridSize):
            print(grids[i - 1])

