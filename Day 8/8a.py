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
    for entry in entries:
        for output in entry["outputs"]:
            if len(output) in [2, 4, 3, 7]:
                sum = sum + 1
    
    print(sum)

if __name__ == "__main__":
    main()