from time import sleep
import os


def parse_input(filename):
    with open(filename) as f:
        input = f.readline()
    return input

def clear():
    sleep(0.001)
    os.system('cls')

def simulation(cave, total_rocks, verbose):
    jet = 0
    shape = 0
    rock_counter = 0
    cave.falling_rock = cave.shapes[shape]
    states = {}
    cycle_found = False
    skipped_cycles = None

    while rock_counter < total_rocks:
        if verbose: cave.draw_grid()
        cave.push_rock(jets[jet])
        if verbose: cave.draw_grid()
        can_fall = cave.drop_rock()

        jet += 1
        if jet == len(jets):
            jet = 0

        if not can_fall:
            rock_counter += 1
            shape += 1
            if shape == 5:
                shape = 0
            cave.falling_rock = cave.shapes[shape]
            
        if not cycle_found:
            state = [x - min(cave.columns) for x in cave.columns]
            state.extend([shape, jet])
            state = tuple(state)
            if state in states:
                cycle_found = True
                height_gain_in_cycle = cave.highest_point - states[state][0]
                rocks_in_cycle = rock_counter - states[state][1]
                skipped_cycles = (total_rocks - rock_counter) // rocks_in_cycle
                rock_counter += skipped_cycles * rocks_in_cycle
            else:
                states[state] = [cave.highest_point, rock_counter]
    
    if skipped_cycles:
        print(cave.highest_point + 1 + skipped_cycles * height_gain_in_cycle)
    else:
        print(cave.highest_point + 1)


class Grid:
    def __init__(self):
        self.width = 7
        self.columns = [-1 for _ in range(self.width)]
        self.highest_point = max(self.columns)
        self.height = 3
        self.walls = self.update_walls()
        self.shapes = self.get_rock_shapes()
        self.fallen_rocks = set()
        self.falling_rock = list()

    def update_walls(self):
        walls = set()
        for row in range(self.height + 4):
            walls.add((row, -1))
            walls.add((row, self.width))
        for col in range(self.width):
            walls.add((-1, col))
        return walls
        
    def draw_grid(self):
        MAX_ROWS_ON_SCREEN = 50
        top = self.height + 3
        bottom = max(top - MAX_ROWS_ON_SCREEN, -1)
        for row in range(top, bottom, -1):
            s = '|'
            for col in range(self.width):
                if (row, col) in self.fallen_rocks:
                    symbol = '#'
                elif (row, col) in self.falling_rock:
                    symbol = '@'
                else:
                    symbol = '.'
                s += symbol
            print(s + '|')
        
        if bottom == -1:
            print('+' + '-' * self.width + '+')
        else:
            print('\n')
        print(f'Current height: {self.highest_point + 1}')
        clear()

    def get_rock_shapes(self):
        shapes = list()
        h = self.height
        shapes.append([(h,2), (h,3), (h,4), (h,5)])
        shapes.append([(h+2,3), (h+1,2), (h+1,3), (h+1,4), (h, 3)])
        shapes.append([(h+2,4), (h+1,4), (h,2), (h,3), (h,4)])
        shapes.append([(h+3,2), (h+2,2), (h+1,2), (h,2)])
        shapes.append([(h+1,2), (h+1,3), (h,2), (h,3)])
        return shapes

    def push_rock(self, direction):
        #update horizontal position
        can_move = True
        pos = self.falling_rock
        if direction == '>':
            new_pos = [(pos[i][0], pos[i][1] + 1) for i in range(len(pos))]
        elif direction == '<':
            new_pos = [(pos[i][0], pos[i][1] - 1) for i in range(len(pos))]
        else:
            print("INPUT ERROR")
            return None
        for i in new_pos:
            if i in self.walls or i in self.fallen_rocks:
                can_move = False
                break
        if can_move:
            self.falling_rock = new_pos
    
    def drop_rock(self):   
        #update vertical position
        can_fall = True
        pos = self.falling_rock
        new_pos = [(pos[i][0] - 1, pos[i][1]) for i in range(len(pos))]
        for i in new_pos:
            if i in self.walls or i in self.fallen_rocks:
                can_fall = False
                break
        if can_fall:
            self.falling_rock = new_pos
        if not can_fall:
            for i in self.falling_rock:
                self.fallen_rocks.add(i)
                if i[0] > self.columns[i[1]]:
                    self.columns[i[1]] = i[0]
            self.highest_point = max(self.columns)
            self.height = self.highest_point + 4
            self.walls = self.update_walls()
            self.shapes = self.get_rock_shapes()
        return can_fall


if __name__ == "__main__":

    jets = parse_input('data.txt')

    ### TASK 1 ###
    total_rocks = 2022
    simulation(Grid(), total_rocks, False)

    ### TASK 2 ###
    total_rocks = 1000000000000
    simulation(Grid(), total_rocks, False)