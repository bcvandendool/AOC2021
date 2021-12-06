def main():
    fish = []
    new_fish = 0

    for i in range(9):
        fish.append(0)


    with open("6a_input.txt", "r") as f:
        text = f.readline().strip().split(",")
        for num in text:
            fish[int(num)] = fish[int(num)] + 1


    for i in range(256):
        new_fish = fish[0]
        for j in range(0, 8):
            fish[j] = fish[j+1]

        fish[6] = fish[6] + new_fish
        fish[8] = new_fish

    print(fish)
    print(sum(fish))


if __name__ == "__main__":
    main()