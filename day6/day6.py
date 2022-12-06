def load_input(filename):
    with open(filename) as f:
        input = [line.rstrip('\n') for line in f]
    return input[0]

def detect_marker(datastream, marker_length):
    for index in range(len(datastream) - marker_length + 1):
        potential_marker = set(datastream[index:index + marker_length])
        if len(potential_marker) == marker_length:
            pos_marker = index + marker_length
            return pos_marker


if __name__ == "__main__":

    datastream = load_input('data.txt')

    ### TASK 1 ###
    pos_packet = detect_marker(datastream, 4)
    print(pos_packet)

    ### TASK 2 ###
    pos_message = detect_marker(datastream, 14)
    print(pos_message)