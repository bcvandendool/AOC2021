def get_lowest_point(matrix):
    minimum = 9
    minimum_idx = (0, 0)
    for idx, list in enumerate(matrix):
        min_val = min(list)
        min_idx = list.index(min_val)
        if min_val == 0:
            return (idx, min_idx)
        else:
            if min_val < minimum:
                minimum = min_val
                minimum_idx = (idx, min_idx)
    return minimum_idx

def grow_basin(matrix, point):
    points = [point]
    size = 0
    for pnt in points:
        # check above
        if pnt[0] > 0 and matrix[pnt[0]-1][pnt[1]] != 9 and not (pnt[0]-1, pnt[1]) in points:
            points.append((pnt[0]-1, pnt[1]))
        # check below
        if pnt[0] < len(matrix) - 1 and matrix[pnt[0]+1][pnt[1]] != 9 and not (pnt[0]+1, pnt[1]) in points:
            points.append((pnt[0]+1, pnt[1]))
        # check left
        if pnt[1] > 0 and matrix[pnt[0]][pnt[1]-1] != 9 and not (pnt[0], pnt[1]-1) in points:
            points.append((pnt[0], pnt[1]-1))
        # check right
        if pnt[1] < len(matrix[0]) - 1 and matrix[pnt[0]][pnt[1]+1] != 9 and not (pnt[0], pnt[1]+1) in points:
            points.append((pnt[0], pnt[1]+1))
        matrix[pnt[0]][pnt[1]] = 9
        size = size + 1
    return matrix, size


def main():
    matrix = []

    with open("9a_input.txt", "r") as f:
        for line in f:
            line_arr = []
            for char in line.strip():
                line_arr.append(int(char))
            matrix.append(line_arr)
    
    largest_basins = [0, 0, 0]
    while True:
        point = get_lowest_point(matrix)
        if matrix[point[0]][point[1]] == 9:
            break
        matrix, size = grow_basin(matrix, point)
        if size > largest_basins[0]:
            largest_basins[2] = largest_basins[1]
            largest_basins[1] = largest_basins[0]
            largest_basins[0] = size
        elif size > largest_basins[1]:
            largest_basins[2] = largest_basins[1]
            largest_basins[1] = size
        elif size > largest_basins[2]:
            largest_basins[2] = size

    print("largest_basins: " + str(largest_basins))
    print("answer: " + str(largest_basins[0] * largest_basins[1] * largest_basins[2]))


if __name__ == "__main__":
    main()