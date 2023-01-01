from queue import Queue

def parse_input(filename):
    with open(filename) as f:
        input = [[i for i in line.rstrip('\n')] for line in f]
    return input

def print_grid(area):
    for row in area:
        s=''
        for col in row:
            s += col
        print(s)

def modify_area_task1(area):
    start, goal = None, None

    for row in range(len(area)):
        for col in range(len(area[row])):
            if area[row][col] == 'S':
                start = (row, col)
                area[row][col] = 'a'
            if area[row][col] == 'E':
                goal = (row, col)
                area[row][col] = 'z'
            if start is not None and goal is not None:
                break
        if start is not None and goal is not None:
            break
    return area, start, goal

def get_neighbours(pos, area):
    neighbours = list()
    if pos[0] > 0:
        n = (pos[0] - 1, pos[1])
        if ord(area[pos[0]][pos[1]]) - ord(area[n[0]][n[1]]) >= -1:
            neighbours.append(n)
    if pos[0] < len(area) - 1:
        n = (pos[0] + 1, pos[1])
        if ord(area[pos[0]][pos[1]]) - ord(area[n[0]][n[1]]) >= -1:
            neighbours.append(n)
    if pos[1] > 0:
        n = (pos[0], pos[1] - 1)
        if ord(area[pos[0]][pos[1]]) - ord(area[n[0]][n[1]]) >= -1:
            neighbours.append(n)
    if pos[1] < len(area[0]) - 1:
        n = (pos[0], pos[1] + 1)
        if ord(area[pos[0]][pos[1]]) - ord(area[n[0]][n[1]]) >= -1:
            neighbours.append(n)
    return neighbours

def breadth_first_search(area, start, goal):
    frontier = Queue()
    came_from = dict()
    frontier.put(start)
    came_from[start] = None

    while not frontier.empty():
        current = frontier.get()

        if current == goal:
            break

        for next in get_neighbours(current, area):
            if next not in came_from:
                frontier.put(next)
                came_from[next] = current

    return came_from

def reconstruct_path(came_from, start, goal):
    current = goal
    path = list()

    while current != start:
        path.append(current)
        current = came_from[current]

    return path

def modify_area_task2(area):
    starting_positions = list()
    goal = None

    for row in range(len(area)):
        for col in range(len(area[row])):
            if area[row][col] == 'S' or area[row][col] == 'a':
                area[row][col] = 'a'
                starting_positions.append((row,col))
            if goal is None:
                if area[row][col] == 'E':
                    goal = (row, col)
                    area[row][col] = 'z'
    return area, starting_positions, goal


if __name__ == "__main__":

    ### TASK 1 ###
    area = parse_input('data.txt')
    area, start, goal = modify_area_task1(area)
    print(start)
    came_from = breadth_first_search(area, start, goal)
    path = reconstruct_path(came_from, start, goal)
    print(f'Path length is {len(path)}.')

    ### TASK 2 ###
    area = parse_input('data.txt')
    area, starting_positions, goal = modify_area_task2(area)

    min_length = len(path)
    for start in starting_positions:
        came_from = breadth_first_search(area, start, goal)
        if goal not in came_from:
            continue
        path = reconstruct_path(came_from, start, goal)
        if len(path) < min_length:
            min_length = len(path)
    print(f'Minimal path length is {min_length}.')