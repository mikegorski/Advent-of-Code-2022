from collections import deque


def load_input(filename):
    with open(filename) as f:
        input = [line.rstrip('\n') for line in f]
    return input

def parse_input(input):
    stacks_list = []
    for line in input:
        if line[1] != '1':
            list = [line[i] for i in range(1, len(line),4)]
            stacks_list.append(list)
        else:
            break
    instructions = []
    for line in input:
        if line[0:4] == 'move':
            list = [int(line.split(' ')[i]) for i in range(1,6,2)]
            instructions.append(list)
    return stacks_list, instructions

def create_stacks(stacks_list):
    stack_count = len(stacks_list[-1])
    stacks = []
    for row in range(stack_count):
        stack = deque()
        for line in stacks_list[::-1]:
            item = line[row]
            if item != ' ': stack.append(item)
        stacks.append(stack)
    return stacks

def move_single_crates(stacks, instructions):
    for line in instructions:
        n_crates = line[0]
        from_stack = line[1] - 1
        to_stack = line[2] - 1
        for crate in range(n_crates):
            moved_crate = stacks[from_stack].pop()
            stacks[to_stack].append(moved_crate)
    return stacks

def move_multiple_crates(stacks, instructions):
    for line in instructions:
        n_crates = line[0]
        from_stack = line[1] - 1
        to_stack = line[2] - 1
        moved_crates = []
        for crate in range(n_crates):
            moved_crates.append(stacks[from_stack].pop())
        for moved_crate in moved_crates[::-1]:
            stacks[to_stack].append(moved_crate)
    return stacks

def get_message(stacks):
    message = ''
    for stack in stacks:
        message += stack[-1]
    print(message)


if __name__ == "__main__":
    
    input_data = load_input('data.txt')
    stacks_list, instructions = parse_input(input_data)

    ### TASK 1 ###
    stacks_initial = create_stacks(stacks_list)
    stacks = move_single_crates(stacks_initial, instructions)
    get_message(stacks)

    ### TASK 2 ###
    stacks_initial = create_stacks(stacks_list)
    stacks = move_multiple_crates(stacks_initial, instructions)
    get_message(stacks)