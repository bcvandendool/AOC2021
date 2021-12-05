def main():
    grid = []
    for i in range(1000):
        grid.append([0 for i in range(1000)])

    with open("5a_input.txt", "r") as f:
        for line in f:
            text = line.split(" -> ")
            index_a = text[0].split(",")
            index_a[0] = int(index_a[0])
            index_a[1] = int(index_a[1])
            index_b = text[1].split(",")
            index_b[0] = int(index_b[0])
            index_b[1] = int(index_b[1])

            if index_a[0] == index_b[0]:
                # x equal, vertical line
                if index_b[1] > index_a[1]:
                    for i in range(index_a[1], index_b[1]+1):
                        grid[index_a[0]][i] = grid[index_a[0]][i] + 1
                else:
                    for i in range(index_b[1], index_a[1]+1):
                        grid[index_a[0]][i] = grid[index_a[0]][i] + 1
            elif index_a[1] == index_b[1]:
                # y equal, horizontal line
                if index_b[0] > index_a[0]:
                    for i in range(index_a[0], index_b[0] + 1):
                        grid[i][index_a[1]] = grid[i][index_a[1]] + 1
                else:
                    for i in range(index_b[0], index_a[0] + 1):
                        grid[i][index_a[1]] = grid[i][index_a[1]] + 1
            else:
                # diagonal line
                if index_b[0] > index_a[0] and index_b[1] > index_a[1]:
                    # a: bottom-left
                    # b: top-right
                    for i in range(index_b[0] - index_a[0] + 1):
                        grid[index_a[0]+i][index_a[1]+i] = grid[index_a[0]+i][index_a[1]+i] + 1
                elif index_b[0] > index_a[0] and index_a[1] > index_b[1]:
                    # a: top-left
                    # b: bottom-right
                    for i in range(index_b[0] - index_a[0] + 1):
                        grid[index_a[0]+i][index_a[1]-i] = grid[index_a[0]+i][index_a[1]-i] + 1
                elif index_a[0] > index_b[0] and index_a[1] > index_b[1]:
                    # a: top-right
                    # b: bottom-left
                    for i in range(index_a[0] - index_b[0] + 1):
                        grid[index_b[0]+i][index_b[1]+i] = grid[index_b[0]+i][index_b[1]+i] + 1
                elif index_a[0] > index_b[0] and index_b[1] > index_a[1]:
                    # a: bottom-right
                    # b: top-left
                    for i in range(index_a[0] - index_b[0] + 1):
                        grid[index_b[0]+i][index_b[1]-i] = grid[index_b[0]+i][index_b[1]-i] + 1

        
        count = 0

        for i in range(1000):
            for j in range(1000):
                if grid[i][j] > 1:
                    count = count + 1

        print("count: " + str(count))


if __name__ == "__main__":
    main()