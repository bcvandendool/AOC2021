def main():
    with open("3a_input.txt", "r") as f:
        numbers = 0
        num_1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        
        for line in f:
            text = line.strip()
            numbers = numbers + 1
            for idx, char in enumerate(text):
                if char == "1":
                    num_1[idx] = num_1[idx] + 1
        
        gamma = "0b"
        epsilon = "0b"

        for num in num_1:
            if num / numbers > 0.5:
                # 1 most common
                gamma = gamma + "1"
                epsilon = epsilon + "0"
            elif num / numbers < 0.5:
                # 0 most common
                gamma = gamma + "0"
                epsilon = epsilon + "1"
            else:
                print("equally likely!")
        
        print("gamma: " + gamma + "(" + str(int(gamma, 2)) + ")")
        print("epsilon: " + epsilon + "(" + str(int(epsilon, 2)) + ")")
        print("mult: " + str(int(gamma, 2) * int(epsilon, 2)))

if __name__ == "__main__":
    main()