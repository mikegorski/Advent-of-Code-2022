def parse_input(filename):
    with open(filename) as f:
        input = [line.rstrip('\n') for line in f]
        parsed = []
        for line in input:
            line = [int(i) for i in line]
            parsed.append(line)
    return parsed

def print_grid(map):
    for row in range(len(map)):
        print([col for col in map[row]])

def look_from_left(in_map, out_map):
    for row in range(1, len(in_map) - 1):
        top_h = in_map[row][0]
        for col in range(1, len(in_map[0]) - 1):
            if in_map[row][col] > top_h:
                out_map[row][col] = 1
                top_h = in_map[row][col]
    return out_map

def look_from_right(in_map, out_map):
    for row in range(1, len(in_map) - 1):
        top_h = in_map[row][-1]
        for col in range(len(in_map[0]) - 2, 0, -1):
            if in_map[row][col] > top_h:
                out_map[row][col] = 1
                top_h = in_map[row][col]
    return out_map

def look_from_bottom(in_map, out_map):
    for col in range(1, len(in_map[0]) - 1):
        top_h = in_map[-1][col]
        for row in range(len(in_map) - 2, 0, -1):
            if in_map[row][col] > top_h:
                out_map[row][col] = 1
                top_h = in_map[row][col]
    return out_map

def look_from_top(in_map, out_map):
    for col in range(1, len(in_map[0]) - 1):
        top_h = in_map[0][col]
        for row in range(1, len(in_map) - 1):
            if in_map[row][col] > top_h:
                out_map[row][col] = 1
                top_h = in_map[row][col]
    return out_map

def count_visible(in_map):
    count = 0
    for row in range(1, len(in_map) - 1):
        for col in range(1, len(in_map[0]) - 1):
            count += in_map[row][col]
    count += 2 * (len(in_map) + len(in_map[0]) - 2)
    return count


if __name__ == "__main__":

    height_map = parse_input('data.txt')
    
    ### TASK 1 ###
    visibility_map = [[0 for _ in range(len(height_map[0]))]
                     for _ in range(len(height_map))]

    visibility_map = look_from_left(height_map, visibility_map)
    visibility_map = look_from_right(height_map, visibility_map)
    visibility_map = look_from_bottom(height_map, visibility_map)
    visibility_map = look_from_top(height_map, visibility_map)
    
    visible_trees_count = count_visible(visibility_map)
    print(f'{visible_trees_count} trees are visible from outside the grid.')

    ### TASK 2 ###
    top_score = 0
    for row in range(1, len(height_map) - 1):
        for col in range(1, len(height_map[0]) - 1):
            score = 1
            
            #look left
            score_left = 0
            for x in range(1, col + 1):
                if height_map[row][col] > height_map[row][col - x]:
                    score_left += 1
                else:
                    score_left += 1
                    break
            score *= score_left

            #look right
            score_right = 0
            for x in range(1, len(height_map[0]) - col):
                if height_map[row][col] > height_map[row][col + x]:
                    score_right += 1
                else:
                    score_right += 1
                    break
            score *= score_right

            #look up
            score_up = 0
            for y in range(1, row + 1):
                if height_map[row][col] > height_map[row - y][col]:
                    score_up += 1
                else:
                    score_up += 1
                    break
            score *= score_up

            #look down
            score_down = 0
            for y in range(1, len(height_map) - row):
                if height_map[row][col] > height_map[row + y][col]:
                    score_down += 1
                else:
                    score_down += 1
                    break
            score *= score_down

            if score > top_score: top_score = score

    print(f'Top scenic score = {top_score}')