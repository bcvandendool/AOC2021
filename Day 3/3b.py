def recurse(numbers, index, common=True):
    if len(numbers) == 1:
        return numbers[0]
    else:
        count = 0
        for number in numbers:
            if number[index] == "1":
                count = count + 1

        criteria = 0
        if count / len(numbers) > 0.5:
            # 1 most common
            criteria = "1"
        elif count / len(numbers) < 0.5:
            # 0 most common
            criteria = "0"
        else:
            # equally likely
            criteria = "1"

        lst = []
        for number in numbers:
            if (number[index] == criteria) == common:
                lst.append(number)
        return recurse(lst, index+1, common)

def main():
    numbers = []
    with open("3a_input.txt", "r") as f:
        for line in f:
            text = line.strip()
            numbers.append(text)

    oxygen = "0b" + recurse(numbers, 0, common=True)
    co2 = "0b" + recurse(numbers, 0, common=False)

    print(oxygen)

    print("oxygen: " + oxygen + "(" + str(int(oxygen, 2)) + ")")
    print("co2: " + co2 + "(" + str(int(co2, 2)) + ")")
    print("mult: " + str(int(oxygen, 2) * int(co2, 2)))


if __name__ == "__main__":
    main()