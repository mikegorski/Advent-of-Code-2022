def load_input(filename):
    with open(filename) as f:
        input = [line.rstrip('\n') for line in f]
    return input[0]

def detect_marker(datastream, marker_length):
    for pos, char in enumerate(datastream):
        potential_marker = datastream[pos:pos + marker_length]
        count_sum = 0
        for char in potential_marker:
            count_sum += potential_marker.count(char)
        if count_sum == marker_length:
            pos_marker = pos + marker_length
            return pos_marker


if __name__ == "__main__":

    datastream = load_input('data.txt')

    ### TASK 1 ###
    pos_packet = detect_marker(datastream, 4)
    print(pos_packet)

    ### TASK 2 ###
    pos_message = detect_marker(datastream, 14)
    print(pos_message)