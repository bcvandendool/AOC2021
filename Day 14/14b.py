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

    polymer_pieces = {}

    for i in range(len(polymer) - 1):
        polymer_pieces[polymer[i] + polymer[i+1]] = polymer_pieces.get(polymer[i] + polymer[i+1], 0) + 1

    counts = {}
    for i in range(len(polymer)):
        counts[polymer[i]] = counts.get(polymer[i], 0) + 1

    for step in range(40):
        new_polymer_pieces = {}
        for key in polymer_pieces.keys():
            new_polymer_pieces[key[0] + mapping[key]] = new_polymer_pieces.get(key[0] + mapping[key], 0) + polymer_pieces[key]
            new_polymer_pieces[mapping[key] + key[1]] = new_polymer_pieces.get(mapping[key] + key[1], 0) + polymer_pieces[key]
            counts[mapping[key]] = counts.get(mapping[key], 0) + polymer_pieces[key]
        polymer_pieces = new_polymer_pieces

    print(counts)
    print("result: " + str(max(counts.values()) - min(counts.values())))


if __name__ == "__main__":
    main()