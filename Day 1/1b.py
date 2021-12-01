def main():
    with open("1a_input.txt", "r") as f:
        sum_1 = -1
        sum_2 = -1
        sum_3 = -1

        increased = 0

        for idx, line in enumerate(f):
            # get current sum
            old_sum = sum_1 + sum_2 + sum_3
            # update values
            sum_1 = sum_2
            sum_2 = sum_3
            sum_3 = int(line)
            # get new sum
            new_sum = sum_1 + sum_2 + sum_3
            # update increased
            if idx > 2 and new_sum > old_sum:
                increased = increased + 1
        
        print(increased)


if __name__ == "__main__":
    main()