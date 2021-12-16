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
        #print(int(literal,2))
        return i+5
    else: # operator
        if packet[6] == "0": # total length in bits
            num_bits = int(packet[7:22], 2)
            offset = 0
            while num_bits > 0:
                length = decode_packet(packet[22 + offset:])
                offset = offset + length
                num_bits = num_bits - length
            return 22 + offset
        else: # number of sub-packets
            num_packets = int(packet[7:18], 2)
            offset = 0
            for i in range(num_packets):
                length = decode_packet(packet[18 + offset:])
                offset = offset + length
            return 18 + offset

def main():
    transmission = ""
    with open("16a_input.txt", "r") as f:
        for line in f:
            for char in line.strip():
                binary = bin(int(char, 16))
                transmission = transmission + str(binary)[2:].zfill(4)

    decode_packet(transmission)

    print("version total: " + str(version_total))

if __name__ == "__main__":
    main()