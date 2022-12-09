from math import sqrt
from numpy import unique, sign

def parse_input(filename):
    with open(filename) as f:
        input = [line.rstrip('\n').split(' ') for line in f]
    return input

def move_head(initial_position, direction):
    position = initial_position
    if direction == 'R':
        position[1] += 1
    elif direction == 'L':
        position[1] -= 1
    if direction == 'U':
        position[0] += 1
    elif direction == 'D':
        position[0] -= 1
    return position

def move_tail(initial_position, head_position):
    position = initial_position
    dist0 = head_position[0] - position[0]
    dist1 = head_position[1] - position[1]
    dist = sqrt(dist0 ** 2 + dist1 ** 2)
    if dist > sqrt(2):
        direction = [sign(dist0), sign(dist1)]
        position[0] = position[0] + 1 * direction[0]
        position[1] = position[1] + 1 * direction[1]
    return position


if __name__ == "__main__":

    instructions = parse_input('data.txt')

    ### TASK 1 ###
    visited_positions = []
    starting_positions = [[0, 0] for _ in range(2)]
    visited_positions.append([i for i in starting_positions[0]])
    
    for direction, n_steps in instructions:
        for step in range(int(n_steps)):
            starting_positions[1] = move_head(starting_positions[1], direction)
            starting_positions[0] = move_tail(starting_positions[0],
                                             starting_positions[1])
            visited_positions.append([i for i in starting_positions[0]])
    
    visited_positions_count = len((unique(visited_positions, axis = 0)))
    print(f'In total {visited_positions_count} positions were visited.')

    ### TASK 2 ###
    visited_positions = []
    starting_positions = [[0, 0] for _ in range(10)]
    visited_positions.append([i for i in starting_positions[0]])
    
    for direction, n_steps in instructions:
        for step in range(int(n_steps)):
            starting_positions[9] = move_head(starting_positions[9], direction)
            for knot in range(8, -1, -1):
                starting_positions[knot] = move_tail(starting_positions[knot],
                                                    starting_positions[knot + 1])
            visited_positions.append([i for i in starting_positions[0]])
    
    visited_positions_count = len((unique(visited_positions, axis = 0)))
    print(f'In total {visited_positions_count} positions were visited.')