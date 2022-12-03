def load_input(filename):
    with open(filename) as input_file:
        input = [line.rstrip('\n') for line in input_file]
        return input

def find_common_items(list1, list2):
    common_items = ''.join(set(list1).intersection(list2))
    return common_items

def letter_to_number(letter):
    number = ord(letter) - 96 if letter.islower() else ord(letter) - 38
    return number


if __name__ == "__main__":

    backpacks = load_input('data.txt')

    ### TASK 1 ###
    total_priority = 0

    for backpack in backpacks:
        length = len(backpack)
        common_item = find_common_items(backpack[:length//2], backpack[length//2:])
        item_priority = letter_to_number(common_item)
        total_priority += item_priority

    print(f'Sum of the priorities in the 1st task: {total_priority}')

    ### TASK 2 ###
    total_priority = 0
    group_size = 3

    for index, backpack in enumerate(backpacks):
        if (index + 1) % group_size == 0:
            elf1, elf2 = backpacks[index-2], backpacks[index-1]
            common_item_12 = find_common_items(elf1, elf2)
            common_item = find_common_items(common_item_12, backpack)
            item_priority = letter_to_number(common_item)
            total_priority += item_priority

    print(f'Sum of the priorities in the 2nd task: {total_priority}')