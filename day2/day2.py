def load_input(filename):
    with open(filename) as input_file:
        input = [line.rstrip('\n') for line in input_file]
        return input

def define_points():
    dict = {'rock': 1, 'paper': 2, 'scissors': 3,
                  'lose': 0, 'draw': 3, 'win': 6}
    return dict

def map_points(task_num, rock, paper, scissors, lose, draw, win):
    if task_num == 1:
        points = {'A X': draw+rock, 'A Y': win+paper, 'A Z': lose+scissors,
                  'B X': lose+rock, 'B Y': draw+paper, 'B Z': win+scissors,
                  'C X': win+rock, 'C Y': lose+paper, 'C Z': draw+scissors}
        return points
    if task_num == 2:
        points = {'A X': lose+scissors, 'A Y': draw+rock, 'A Z': win+paper,
                  'B X': lose+rock, 'B Y': draw+paper, 'B Z': win+scissors,
                  'C X': lose+paper, 'C Y': draw+scissors, 'C Z': win+rock}
        return points
    else:
        print("ERROR")


if __name__ == "__main__":

    match_list = load_input('data.txt')

    ### TASK 1 ###
    task_num = 1
    points_mapping = map_points(task_num, **define_points())

    total_score = 0
    for match in match_list:
        total_score += points_mapping[match]
    print(f'The total score in task {task_num} is {total_score}')

    ### TASK 2 ###
    task_num = 2
    points_mapping = map_points(task_num, **define_points())

    total_score = 0
    for match in match_list:
        total_score += points_mapping[match]
    print(f'The total score in task {task_num} is {total_score}')