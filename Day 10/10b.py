def main():
    with open("10a_input.txt", "r") as f:
        scores = []
        for line in f:
            stack = []
            sum = 0
            score = 0
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

            if len(stack) != 0 and sum == 0:
                while len(stack) != 0:
                    char = stack.pop()
                    if char == "(":
                        score = score * 5 + 1
                    elif char == "[":
                        score = score * 5 + 2
                    elif char == "{":
                        score = score * 5 + 3
                    elif char == "<":
                        score = score * 5 + 4
                scores.append(score)

        scores = sorted(scores)
        print("score: " + str(scores[(len(scores) // 2)]))

if __name__ == "__main__":
    main()