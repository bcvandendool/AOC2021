import heapdict

def main():
    grid = []
    grid_distances = []

    with open("15a_input.txt", "r") as f:
        for line in f:
            grid_line = []
            grid_distances_line = []
            for char in line.strip():
                grid_line.append(int(char))
                grid_distances_line.append(999999999)
            grid.append(grid_line)
            grid_distances.append(grid_distances_line)

    new_grid = []
    grid_distances = []

    for y in range(len(grid) * 5):
        grid_line = []
        grid_distances_line = []
        for x in range(len(grid[0]) * 5):
            value = grid[y % len(grid)][x % len(grid[0])] + y//len(grid) + x//len(grid[0])
            if value > 9:
                value = value - 9
            grid_line.append(value)
            grid_distances_line.append(999999999)
        new_grid.append(grid_line)
        grid_distances.append(grid_distances_line)

    grid = new_grid

    grid_distances[0][0] = 0

    visited_nodes = set()
    queue = heapdict.heapdict()

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            queue[(j, i)] = 999999999

    queue[(0,0)] = 0

    def relax(u, v):
        if grid_distances[u[0]][u[1]] + grid[v[0]][v[1]] < grid_distances[v[0]][v[1]]:
            grid_distances[v[0]][v[1]] = grid_distances[u[0]][u[1]] + grid[v[0]][v[1]]
            queue[(v)] = grid_distances[v[0]][v[1]]

    while queue:
        #print(len(queue))
        min_val = queue.popitem()
        #visited_nodes = visited_nodes | {min_val[0]}
        # left
        if min_val[0][0] > 0:
            relax(min_val[0], (min_val[0][0] - 1, min_val[0][1]))
        # right
        if min_val[0][0] < len(grid[0])-1:
            relax(min_val[0], (min_val[0][0] + 1, min_val[0][1]))
        # up
        if min_val[0][1] > 0:
            relax(min_val[0], (min_val[0][0], min_val[0][1] - 1))
        # down
        if min_val[0][1] < len(grid)-1:
            relax(min_val[0], (min_val[0][0], min_val[0][1] + 1))

    print(grid_distances[len(grid_distances)-1][len(grid_distances[0])-1])



if __name__ == "__main__":
    main()