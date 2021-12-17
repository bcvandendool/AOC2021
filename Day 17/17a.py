def main():
    x_min = 0
    x_max = 0
    y_min = 0
    y_max = 0

    with open("17a_input.txt", "r") as f:
        line = f.readline().strip()
        segments = line.split()
        seg_x = segments[2].split("=")[1]
        x_min = int(seg_x[:-1].split("..")[0])
        x_max = int(seg_x[:-1].split("..")[1])
        seg_y = segments[3].split("=")[1]
        y_min = int(seg_y.split("..")[0])
        y_max = int(seg_y.split("..")[1])

    print(x_min)
    print(x_max)
    print(y_min)
    print(y_max)

    best_y = 0
    best_start_x = 0
    best_start_y = 0

    for x in range(0, 1000):
        for y in range(-1000, 2000):
            vel_x = x
            vel_y = y

            pos_x = 0
            pos_y = 0

            cur_max = 0

            for t in range(800):
                if vel_x == 0 and not (pos_x >= x_min and pos_x <= x_max):
                    break
                pos_x = pos_x + vel_x
                pos_y = pos_y + vel_y


                if pos_y > cur_max:
                    cur_max = pos_y
                    # if cur_max > best_y:
                    #     print("found higher y: " + str(cur_max))


                if vel_x > 0:
                    vel_x = vel_x - 1
                elif vel_x < 0:
                    vel_x = vel_x + 1

                vel_y = vel_y - 1

                if pos_x > x_max or pos_y < y_min:
                    break

                if pos_x >= x_min and pos_x <= x_max and pos_y >= y_min and pos_y <= y_max:
                    if cur_max > best_y:
                        best_y = cur_max
                        best_start_x = x
                        best_start_y = y
                    break

    print(best_y)
    print(best_start_x)
    print(best_start_y)



if __name__ == "__main__":
    main()