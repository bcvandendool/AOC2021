def main():
    locations = []

    with open("7a_input.txt", "r") as f:
        text = f.readline()
        for num in text.split(","):
            locations.append(int(num))

    min_pos = -1
    min_fuel = 999999999999999

    for i in range(min(locations), max(locations) + 1):
        sum = 0
        for loc in locations:
            sum = sum + abs(loc - i)
        if sum < min_fuel:
            min_pos = i
            min_fuel = sum

    print("min_pos: " + str(min_pos))
    print("min_fuel: " + str(min_fuel))


if __name__ == "__main__":
    main()