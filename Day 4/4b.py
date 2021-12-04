def main():
    numbers = []
    grids = []

    with open("4a_input.txt") as f:
        numbers_input = f.readline()
        for number in numbers_input.strip().split(","):
            numbers.append(int(number))

        # read whiteline
        f.readline()

        grid = []
        row = []

        for line in f:
            if line.strip() == "":
                grids.append(grid)
                grid = []
            else:
                for number in line.strip().split():
                    row.append(int(number))
                grid.append(row)
                row = []

    for i in range(len(numbers)):
        for grid in grids:
            if check_grid(grid, numbers[:i]) and len(grids) == 1:
                flat = [item for sublist in grid for item in sublist]
                summed = [num for num in flat if num not in numbers[:i]]
                Sum = sum(summed)
                print("grid:")
                print(grid)
                print("numbers:")
                print(numbers[:i])
                print("Sum: " + str(Sum))
                print("number: " + str(numbers[i-1]))
                print("result: " + str(Sum * numbers[i-1]))
                return
            elif check_grid(grid, numbers[:i]):
                grids.remove(grid)



def check_grid(grid, numbers):
    # check rows
    for i in range(5):
        if all(elem in numbers for elem in grid[i]):
            return True
    # check columns
    for i in range(5):
        temp = []
        for j in range(5):
            temp.append(grid[j][i])
        if all(elem in numbers for elem in temp):
            return True

    return False

if __name__ == "__main__":
    main()