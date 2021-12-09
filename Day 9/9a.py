def main():
    matrix = []

    with open("9a_input.txt", "r") as f:
        for line in f:
            line_arr = []
            for char in line.strip():
                line_arr.append(int(char))
            matrix.append(line_arr)
    
    risk = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            # check above
            if i > 0 and matrix[i-1][j] <= matrix[i][j]:
                continue
            # check below
            if i < len(matrix) - 1 and matrix[i+1][j] <= matrix[i][j]:
                continue
            # check left
            if j > 0 and matrix[i][j-1] <= matrix[i][j]:
                continue
            # check right
            if j < len(matrix[0]) - 1 and matrix[i][j+1] <= matrix[i][j]:
                continue
            risk = risk + matrix[i][j] + 1

    print("risk: " + str(risk))


if __name__ == "__main__":
    main()