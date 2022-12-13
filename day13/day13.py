import json

def parse_input(filename):
    with open(filename) as f:
        input = [line.rstrip('\n') for line in f]
        input = [json.loads(line) for line in input if line != '']
    return input

def compare(left, right):
    length = max(len(left), len(right))
    
    for i in range(length):
        result = None
        try:
            check = left[i]
        except IndexError:
            return True
        try:
            check = right[i]
        except IndexError:
            return False

        if type(left[i]) == type(right[i]) == int:
            if left[i] < right[i]:
                return True
            if left[i] > right[i]:
                return False
        elif type(left[i]) == type(right[i]) == list:
            result = compare(left[i], right[i])
        elif type(left[i]) != type(right[i]):
            if type(left[i]) == int:
                result = compare([left[i]], right[i])
            if type(right[i]) == int:
                result = compare(left[i], [right[i]])
    
        if result is not None:
            return result

def sort_signal(signal):
    for i in range(len(signal)):
        already_sorted = True
        for j in range(len(signal) - i - 1):
            if not compare(signal[j], signal[j + 1]):
                signal[j], signal[j + 1] = signal[j + 1], signal[j]
                already_sorted = False
        if already_sorted: break
    return signal


if __name__ == "__main__":

    signal = parse_input('data.txt')

    ### TASK 1 ###
    pair_num = 0
    total = 0

    for i in range(0, len(signal), 2):
        pair_num += 1
        if compare(signal[i], signal[i + 1]):
            total += pair_num

    print(f'Sum of the indices of packet pairs in correct order is {total}.')

    ### TASK 2 ###
    signal.append([[2]])
    signal.append([[6]])

    signal = sort_signal(signal)

    decoder_key = 1
    for idx, line in enumerate(signal):
        if line == [[2]] or line == [[6]]:
            decoder_key *= idx + 1

    print(f'The decoder key is {decoder_key}.')