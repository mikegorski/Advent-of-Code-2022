def parse_input(filename):
    with open(filename) as f:
        input = [int(line.rstrip('\n')) for line in f]
    return input

def mix_data(data, rounds, key):

    indices = [i for i in range(len(data))]

    for round in range(rounds):
        for i, num in enumerate(data):
            target_pos = (indices.index(i) + num * key) % (len(data) - 1)
            if target_pos == 0 or target_pos == len(data) - 1:
                indices = [x for x in indices if x != i] + [i]
            else:
                if target_pos > indices.index(i):
                    indices = [x for x in indices[:target_pos+1] if x != i] + [i] \
                            + [x for x in indices[target_pos+1:] if x != i]
                elif target_pos < indices.index(i):
                    indices = [x for x in indices[:target_pos] if x != i] + [i] \
                            + [x for x in indices[target_pos:] if x != i]
     
    data_sorted = [data[z] for z in indices]

    grove_coords_sum = 0
    for c in range(1,4):
        num = data_sorted.index(0) + c*1000 % len(data)
        if num > (len(data) - 1): num -= len(data)
        grove_coords_sum += data_sorted[num] * key

    print(grove_coords_sum)


if __name__ == "__main__":

    data = parse_input('data.txt')
    
    ### TASK 1 ###
    mix_data(data, 1, 1)

    ### TASK 2 ###
    mix_data(data, 10, 811589153)