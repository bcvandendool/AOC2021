def print_grid(points):
    max_x = 0
    max_y = 0

    for point in points:
        if point[0] > max_x:
            max_x = point[0]
        if point[1] > max_y:
            max_y = point[1]

    for y in range(max_y+1):
        for x in range(max_x+1):
            if (x, y) in points:
                print("#", end="")
            else:
                print(" ", end="")
        print("")


def main():
    points = set()
    folds = []

    with open("13a_input.txt", "r") as f:
        for line in f:
            if line.strip() == "":
                pass
            elif line.strip().startswith("fold"):
                text = line.strip().split()
                text = text[2].split("=")
                folds.append({"direction": text[0], "value": int(text[1])})
            else:
                point = line.strip().split(",")
                points.add((int(point[0]), int(point[1])))

    for fold in folds:
        new_points = set()
        for point in points:
            if fold["direction"] == "x":
                if point[0] > fold["value"]:
                    new_points.add((fold["value"] - (point[0] - fold["value"]), point[1]))
                else:
                    new_points.add(point)
            elif fold["direction"] == "y":
                if point[1] > fold["value"]:
                    new_points.add((point[0], fold["value"] - (point[1] - fold["value"])))
                else:
                    new_points.add(point)
        points = new_points

    print_grid(points)


if __name__ == "__main__":
    main()