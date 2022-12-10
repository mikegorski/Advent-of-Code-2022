class Screen:
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.pixels = [['.' for _ in range(width)] for _ in range(height)]

    def render(self):
        string = ''
        for row in range(self.height):
            for col in range(self.width):
                string += self.pixels[row][col]
            string += '\n'
        print(string)

    def draw_pixel(self, cycle, X): 
        col = (cycle - 1) % self.width
        if col in [X - 1, X, X + 1]:
            row = (cycle - 1) // self.width
            self.pixels[row][col] = '#'


def parse_input(filename):
    with open(filename) as f:
        data = [line.rstrip().split(' ') for line in f]
    return data


if __name__ == "__main__":

    program = parse_input('data.txt')

    X = 1
    cycle = 0
    sum_of_signals = 0
    screen = Screen(40, 6)

    for line in program:
        cycle += 1
        screen.draw_pixel(cycle, X)
        if cycle in [_ for _ in range(20, 221, 40)]:
            sig_str = cycle * X
            sum_of_signals += sig_str
        if line[0] == 'addx':
            cycle += 1
            screen.draw_pixel(cycle, X)
            if cycle in [_ for _ in range(20, 221, 40)]:
                sig_str = cycle * X
                sum_of_signals += sig_str
            X += int(line[1])
     
    ### TASK 1 ###
    print(f'Sum of signals is {sum_of_signals}\n')
    ### TASK 2 ###
    screen.render()