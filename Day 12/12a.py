def count_path(graph, node, visited):
    if node == "end":
        return 1
    else:
        options = graph[node]
        sum = 0
        for option in options:
            if (option in visited and option.islower()) or (option == "start"):
                continue
            else:
                sum = sum + count_path(graph, option, visited | {option})
        return sum

def main():
    graph = {}
    with open("12a_input.txt", "r") as f:
        for line in f:
            text = line.strip().split("-")

            if text[0] in graph:
                graph[text[0]].append(text[1])
            else:
                graph[text[0]] = [text[1]]

            if text[1] in graph:
                graph[text[1]].append(text[0])
            else:
                graph[text[1]] = [text[0]]

    print(graph)
    result = count_path(graph, "start", set())
    print("result: " + str(result))


if __name__ == "__main__":
    main()