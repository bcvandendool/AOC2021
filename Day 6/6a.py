def main():
    fish = []
    with open("6a_input.txt", "r") as f:
        text = f.readline().strip().split(",")
        for num in text:
            fish.append(int(num))

    new_fish = []
    for j in range(80):
        for i in range(len(fish)):
            if fish[i] == 0:
                new_fish.append(8)
                fish[i] = 6
            else:
                fish[i] = fish[i] - 1
        fish = fish + new_fish
        new_fish = []

    print(len(fish))

if __name__ == "__main__":
    main()