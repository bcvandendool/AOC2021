def main():
    with open("1a_input.txt", "r") as f:
        prev = -1
        cur = -1
        increased = 0
        for line in f:
            prev = cur
            cur = int(line)
            if prev != -1 and cur > prev:
                increased = increased + 1
        print(increased)


if __name__ == "__main__":
    main()