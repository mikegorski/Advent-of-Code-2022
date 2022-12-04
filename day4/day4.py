def load_input(filename):
    with open(filename) as input_file:
        input = [line.rstrip('\n') for line in input_file]
    return input

def split_into_sections(pair):
    split = pair.split(',')
    sec1, sec2 = split[0].split('-'), split[1].split('-')
    sec1 = [int(x) for x in sec1]
    sec2 = [int(x) for x in sec2]
    return sec1, sec2

def is_overlap(sec1, sec2):
    range1 = range(sec1[0], sec1[1]+1)
    range2 = range(sec2[0], sec2[1]+1)
    cond1 = (sec1[0] in range2 or sec1[1] in range2)
    cond2 = (sec2[0] in range1 or sec2[1] in range1)
    return cond1 or cond2

def is_duplicate(sec1, sec2):
    range1 = range(sec1[0], sec1[1]+1)
    range2 = range(sec2[0], sec2[1]+1)
    cond1 = (sec1[0] in range2 and sec1[1] in range2)
    cond2 = (sec2[0] in range1 and sec2[1] in range1)
    return cond1 or cond2


if __name__ == "__main__":

    pairs = load_input('data.txt')

    duplicated_pairs_count = 0
    overlapping_pairs_count = 0

    for pair in pairs:
        sec1,sec2 = split_into_sections(pair)
        if is_duplicate(sec1,sec2): duplicated_pairs_count += 1
        if is_overlap(sec1,sec2): overlapping_pairs_count += 1

    print(f'Duplicated pairs: {duplicated_pairs_count}')
    print(f'Overlapping pairs: {overlapping_pairs_count}')