def separate_inputs(set):
    x, y = (set.split(' '))
    return int(x), int(y)

if __name__ == "__main__":
    x ,y =(separate_inputs("2 3"))
    print(x , type(y))
