version_total = 0

def decode_packet(packet):
    version = int(packet[:3], 2)
    global version_total
    version_total = version_total + version
    type = int(packet[3:6], 2)

    if type == 4: # literal
        i = 6
        literal = ""
        while packet[i] == "1":
            section = packet[i+1:i+5]
            literal = literal + section
            i = i + 5
        # last section, starts with '0'
        section = packet[i+1:i+5]
        literal = literal + section
        return int(literal,2), i+5
    else: # operator
        results = []
        result_length = 0
        
        if packet[6] == "0": # total length in bits
            num_bits = int(packet[7:22], 2)
            offset = 0
            while num_bits > 0:
                result, length = decode_packet(packet[22 + offset:])
                results.append(result)
                offset = offset + length
                num_bits = num_bits - length
            result_length =  22 + offset
        else: # number of sub-packets
            num_packets = int(packet[7:18], 2)
            offset = 0
            for i in range(num_packets):
                result, length = decode_packet(packet[18 + offset:])
                results.append(result)
                offset = offset + length
            result_length = 18 + offset
        
        res = 0
        if type == 0: # sum
            for temp in results:
                res = res + temp
        elif type == 1: # product
            for idx, temp in enumerate(results):
                if idx == 0:
                    res = temp
                else:
                    res = res * temp
        elif type == 2: # min
            res = min(results)
        elif type == 3: # max
            res = max(results)
        elif type == 5: # greater than
            if results[0] > results[1]:
                res = 1
            else:
                res = 0
        elif type == 6: # less than
            if results[1] > results[0]:
                res = 1
            else:
                res = 0
        elif type == 7: # equal to
            if results[0] == results[1]:
                res = 1
            else:
                res = 0

        return res, result_length

def main():
    transmission = ""
    with open("16a_input.txt", "r") as f:
        for line in f:
            for char in line.strip():
                binary = bin(int(char, 16))
                transmission = transmission + str(binary)[2:].zfill(4)

    result, _ = decode_packet(transmission)

    print("result: " + str(result))

if __name__ == "__main__":
    main()