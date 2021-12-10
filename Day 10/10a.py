def main():
    with open("10a_input.txt", "r") as f:
        sum = 0
        for line in f:
            stack = []
            for char in line.strip():
                if char in ["(", "[", "{", "<"]:
                    stack.append(char)
                elif char == ")":
                    if stack[-1] == "(":
                        stack.pop()
                    else:
                        sum = sum + 3
                        break
                elif char == "]":
                    if stack[-1] == "[":
                        stack.pop()
                    else:
                        sum = sum + 57
                        break
                elif char == "}":
                    if stack[-1] == "{":
                        stack.pop()
                    else:
                        sum = sum + 1197
                        break
                elif char == ">":
                    if stack[-1] == "<":
                        stack.pop()
                    else:
                        sum = sum + 25137
                        break
                else:
                    print("wtf!?")

        print("sum: " + str(sum))

if __name__ == "__main__":
    main()