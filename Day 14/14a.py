def main():
    polymer = []
    mapping = {}

    with open("14a_input.txt", "r") as f:
        input = f.readline()
        for char in input.strip():
            polymer.append(char)
        f.readline()
        for line in f:
            text = line.strip().split(" -> ")
            mapping[text[0]] = text[1]

    for step in range(10):
        new_polymer = [polymer[0]]
        for i in range(len(polymer) - 1):
            new_polymer.append(mapping[polymer[i] + polymer[i+1]])
            new_polymer.append(polymer[i+1])
        polymer = new_polymer

    counts = {}
    for i in range(len(polymer)):
        counts[polymer[i]] = counts.get(polymer[i], 0) + 1

    print("result: " + str(max(counts.values()) - min(counts.values())))


if __name__ == "__main__":
    main()