import math

def find_first_number_after(number, index):
    start_idx = len(number)
    end_idx = len(number)

    for i in range(index, len(number)):
        if number[i].isnumeric():
            start_idx = i
            break
    
    end_idx = start_idx
    for i in range(start_idx + 1, len(number)):
        if number[i].isnumeric():
            end_idx = end_idx + 1
        else:
            break
    
    return start_idx, end_idx
            
def find_first_number_before(number, index):
    start_idx = 0
    end_idx = 0

    for i in range(index, 0, -1):
        if number[i].isnumeric():
            end_idx = i
            break
    
    start_idx = end_idx
    for i in range(start_idx - 1, 0, -1):
        if number[i].isnumeric():
            start_idx = start_idx - 1
        else:
            break
    
    return start_idx, end_idx

def explode_number(number):
    num_open = 0

    start_pair = 0
    end_pair = 0

    for i in range(len(number)):
        if number[i] == "[":
            num_open = num_open + 1
        elif number[i] == "]":
            num_open = num_open - 1
        
        if num_open == 5:
            start_pair = i
            break

    if start_pair == 0:
        return number, False

    for i in range(start_pair, len(number)):
        if number[i] == "]":
            end_pair = i
            break
    
    pair = number[start_pair:end_pair+1]
    idx_comma = number.find(",", start_pair, end_pair+1)
    before_start, before_end = find_first_number_before(number, start_pair)
    after_start, after_end = find_first_number_after(number, end_pair)

    replace_before = number[before_start:before_end+1]
    replace_pair = "0"
    replace_after = number[after_start:after_end+1]

    if before_end > 0:
        replace_before = str(int(number[before_start:before_end+1]) + int(number[start_pair+1:idx_comma]))

    if after_start < len(number):
        replace_after = str(int(number[after_start:after_end+1]) + int(number[idx_comma+1:end_pair]))

    return number[:before_start] + replace_before + number[before_end+1:start_pair] + replace_pair + number[end_pair+1:after_start] + replace_after + number[after_end+1:], True

def split_number(number):
    start, end = find_first_number_after(number,0)
    while end < len(number):
        if int(number[start:end+1]) > 9:

            return number[:start] + "[" + str(math.floor(int(number[start:end+1]) / 2)) + "," + str(math.ceil(int(number[start:end+1]) / 2)) + "]" + number[end+1:], True
        else:
            start, end = find_first_number_after(number, end+1)

    return number, False
    

def add_numbers(num_a, num_b):
    num_c = "[" + num_a + "," + num_b + "]"

    changed = True
    while changed:
        num_c, changed = explode_number(num_c)
        if changed:
            continue

        num_c, changed = split_number(num_c)
    return num_c

def find_separator(number):
    num_open = 0
    for i in range(len(number)):
        if number[i] == "[":
            num_open = num_open + 1
        elif number[i] == "]":
            num_open = num_open - 1

        if num_open == 0:
            return i

def magnitude_number(number):
    if number.isnumeric():
        return int(number)
    else:
        idx = find_separator(number[1:-1])
        sum = 3 * magnitude_number(number[1:idx+2])
        sum = sum + 2 * magnitude_number(number[idx+3:-1])
        return sum

def main():
    numbers = []
    with open("18a_input.txt", "r") as f:
        for line in f:
            numbers.append(line.strip())

    final_number = numbers[0]
    for i in range(1, len(numbers)):
        final_number = add_numbers(final_number, numbers[i])
        print(final_number)

    print(final_number)

    magnitude = magnitude_number(final_number)
    print("magnitude: " + str(magnitude))


if __name__ == "__main__":
    main()