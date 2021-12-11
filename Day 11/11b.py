def get_to_flash(grid):
    to_flash = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] > 9:
                to_flash.append((i, j))
    return to_flash

def all_zero(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] != 0:
                return False
    return True

def main():
    grid = []
    num_flashed = 0

    with open("11a_input.txt", "r") as f:
        for line in f:
            grid_line = []
            for char in line.strip():
                grid_line.append(int(char))
            grid.append(grid_line)

    for step in range(1000):
        if all_zero(grid):
            print("all flashed at step: " + str(step))
            break
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                grid[i][j] = grid[i][j] + 1

        to_flash = get_to_flash(grid)
        while len(to_flash) != 0:
            octo = to_flash[0]
            to_flash.remove(octo)
            num_flashed = num_flashed + 1

            # update octi around
            octi = set()
            for i in range(9):
                x_coord = min(9, max(0, octo[0] - 1 + i % 3))
                y_coord = min(9, max(0, octo[1] - 1 + i // 3))
                octi.add((x_coord, y_coord))

            for elem in octi:
                grid[elem[0]][elem[1]] = grid[elem[0]][elem[1]] + 1
                if grid[elem[0]][elem[1]] == 10:
                    to_flash.append(elem)

        flashed = get_to_flash(grid)
        for elem in flashed:
            grid[elem[0]][elem[1]] = 0


if __name__ == "__main__":
    main()