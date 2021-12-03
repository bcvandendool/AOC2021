def main():
    with open("2a_input.txt", "r") as f:
        horizontal = 0
        depth = 0

        for line in f:
            text = line.split()
            if text[0] == "forward":
                horizontal = horizontal + int(text[1])
            elif text[0] == "down":
                depth = depth + int(text[1])
            elif text[0] == "up":
                depth = depth - int(text[1])
            else:
                print("Unknown command: " + line)
        
        print("horizontal: " + str(horizontal))
        print("depth: " + str(depth))
        print("mult: " + str(horizontal * depth))

if __name__ == "__main__":
    main()