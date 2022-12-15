def parse_input(filename):
    with open(filename) as f:
        input = [line.rstrip('\n').split(' -> ') for line in f]
        coord_lines = []
        x_min, x_max, y_max = 500, 500, 0 
        for line in input:
            coord_line = []
            for item in line:
                x = int(item.split(',')[0])
                y = int(item.split(',')[1])
                if x < x_min: x_min = x
                if x > x_max: x_max = x
                if y > y_max: y_max = y
                coord = (x, y)
                coord_line.append(coord)
            coord_lines.append(coord_line)
            loc_min, loc_max = (x_min, 0), (x_max, y_max)
    return loc_min, loc_max, coord_lines

def sign(x):
    if x == 0: return 0
    return int(x / abs(x))

class SquareGrid:
    def __init__(self, loc_min, loc_max, rock_coords):
        self.loc_min = (loc_min[0] - 10, loc_min[1])
        self.loc_max = (loc_max[0] + 10, loc_max[1] + 2)
        self.walls = self.create_walls(rock_coords)
        self.sand_blocks = set()

    def create_walls(self, rock_coords):
        walls = []
        for line in rock_coords:
            for idx in range(len(line) - 1):
                start = line[idx]
                end = line[idx + 1]
                dir = (sign(end[0] - start[0]), sign(end[1] - start[1]))
                (x, y) = start
                i = 0
                while (x, y) != end:
                    (x, y) = (start[0] + i * dir[0], start[1] + i * dir[1])
                    if (x, y) not in walls: walls.append((x, y))
                    i += 1
        for x in range(self.loc_min[0] - 500, self.loc_max[0] + 500):
            walls.append((x, self.loc_max[1]))
        return set(walls)

    def draw_grid(self):
        for y in range(self.loc_min[1], self.loc_max[1] + 1):
            s = ''
            for x in range(self.loc_min[0], self.loc_max[0] + 1):
                if (x, y) in self.walls:
                    symbol = '#'
                elif (x, y) in self.sand_blocks:
                    symbol = 'o'
                else:
                    symbol = '.'
                s += symbol
            print(s)
        #print('*' * (self.loc_max[0] - self.loc_min[0]))
    
    def simulate_task1(self):
        starting_position = (500, 0)
        current_position = starting_position
        can_move = True
        dirs = [(0, 1), (-1, 1), (1, 1)]
        while current_position[1] < self.loc_max[1] - 2:
            if can_move == False:
                self.sand_blocks.add(current_position)
                current_position = starting_position
                can_move = True
            target = (current_position[0] + dirs[0][0],
                     current_position[1] + dirs[0][1])
            if target not in self.walls and target not in self.sand_blocks:
                current_position = target
            else:
                target = (current_position[0] + dirs[1][0],
                     current_position[1] + dirs[1][1])
                if target not in self.walls and target not in self.sand_blocks:
                    current_position = target
                else:
                    target = (current_position[0] + dirs[2][0],
                     current_position[1] + dirs[2][1])
                    if target not in self.walls and target not in self.sand_blocks:
                        current_position = target
                    else:
                        can_move = False

    def simulate_task2(self):
        starting_position = (500, 0)
        current_position = starting_position
        can_move = True
        dirs = [(0, 1), (-1, 1), (1, 1)]
        while True:
            if can_move == False:
                self.sand_blocks.add(current_position)
                if current_position == starting_position:
                    break
                current_position = starting_position
                can_move = True
            target = (current_position[0] + dirs[0][0],
                     current_position[1] + dirs[0][1])
            if target not in self.walls and target not in self.sand_blocks:
                current_position = target
            else:
                target = (current_position[0] + dirs[1][0],
                     current_position[1] + dirs[1][1])
                if target not in self.walls and target not in self.sand_blocks:
                    current_position = target
                else:
                    target = (current_position[0] + dirs[2][0],
                     current_position[1] + dirs[2][1])
                    if target not in self.walls and target not in self.sand_blocks:
                        current_position = target
                    else:
                        can_move = False


if __name__ == "__main__":

    #loc_min, loc_max, rock_coords = parse_input('data.txt')
    ### TASK 1 ###
    cave = SquareGrid(*parse_input('data.txt'))
    cave.simulate_task1()
    print(f'{len(cave.sand_blocks)} units of sand come to rest.')

    ### TASK 2 ###
    cave = SquareGrid(*parse_input('data.txt'))
    cave.simulate_task2()
    print(f'{len(cave.sand_blocks)} units of sand come to rest.')