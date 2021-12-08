def apply_map(signals, mapping):
    test = set()

    for signal in signals:
        test.add("".join(sorted([mapping[char] for char in signal])))

    return test

def apply_map2(signals, mapping):
    test = []

    for signal in signals:
        test.append("".join(sorted([mapping[char] for char in signal])))

    return test

def recurse(mapping, cur_letter, numbers, signals):
    if mapping['g'] != '':
        if set(apply_map(signals, mapping)) == numbers:
            return mapping
        else:
            return {}
    else:
        for char in "abcdefg":
            if char not in mapping.values():
                mapping["abcdefg"[cur_letter]] = char
                if recurse(mapping, cur_letter + 1, numbers, signals) != {}:
                    return mapping
                mapping["abcdefg"[cur_letter]] = ''
        return {}

def main():
    entries = []
    with open("8a_input.txt", "r") as f:
        for line in f:
            signals = []
            outputs = []

            text = line.split(" | ")
            for signal in text[0].split():
                signals.append(signal)
            for output in text[1].split():
                outputs.append(output)

            entries.append({"signals": signals, "outputs": outputs})

    sum = 0
    numbers = {'abcefg', 'cf', 'acdeg', 'acdfg', 'bcdf', 'abdfg', 'abdefg', 'acf', 'abcdefg', 'abcdfg'}
    numbers_lst = ['abcefg', 'cf', 'acdeg', 'acdfg', 'bcdf', 'abdfg', 'abdefg', 'acf', 'abcdefg', 'abcdfg']
    for entry in entries:
        mapping = {'a': '', 'b': '', 'c': '', 'd': '', 'e': '', 'f': '', 'g': ''}
        mapping = recurse(mapping, 0, numbers, entry["signals"])

        #print(entries[0]["outputs"])
        output = apply_map2(entry["outputs"], mapping)
        output = [numbers_lst.index(item) for item in output]
        print(entry["outputs"])
        print(output)

        sum = sum + output[0] * 1000 + output[1] * 100 + output[2] * 10 + output[3]

    print("sum: " + str(sum))


if __name__ == "__main__":
    main()