def parse_input(filename):
    with open(filename) as f:
        input = [line.strip() for line in f]
        monkeys = []
        for line in input[1:]:
            if line.startswith('Starting'):
                monkey = []
                list = [int(i) for i in line[line.find(':') + 2:].split(', ')]
                monkey.append(list)
            if line.startswith('Operation'):
                expression = line[line.find('=') + 2:].replace('old', 'item')
                monkey.append(expression)
            if line.startswith('Test'):
                div_by = int(line[line.find('by') + 3:])
                monkey.append(div_by)
            if line.startswith('If true'):
                true_cond = int(line[line.find('monkey') + 7:])
                monkey.append(true_cond)
            if line.startswith('If false'):
                false_cond = int(line[line.find('monkey') + 7:])
                monkey.append(false_cond)
            if line.startswith('Monkey'):
                monkeys.append(monkey)
        monkeys.append(monkey)
    return monkeys

def calculate_monkey_business_level(task_num):
    monkeys = parse_input('data.txt')
    inspect_count = [0 for _ in range(len(monkeys))]
    round = 0
    
    if task_num == 1:
        max_rounds = 20
    elif task_num == 2:
        max_rounds = 10000
        max_worry = 1
        for monkey in monkeys:
            max_worry *= monkey[2]
    else:
        print("Error - task number can either be 1 or 2.")
        return None

    while round < max_rounds:
        round += 1
        for monkey in monkeys:
            idx = monkeys.index(monkey)
            for item in monkey[0]:
                inspect_count[idx] += 1
                if task_num == 1:
                    worry_level = eval(monkey[1]) // 3
                else:
                    worry_level = eval(monkey[1]) % max_worry
                if worry_level % monkey[2] == 0:
                    monkeys[monkey[3]][0].append(worry_level)
                else:
                    monkeys[monkey[4]][0].append(worry_level)  
            monkey[0] = []
    inspect_count.sort(reverse = True)
    monkey_business = inspect_count[0] * inspect_count[1]
    print(f'The level of monkey business in task {task_num} is {monkey_business}.')


if __name__ == "__main__":

    ### TASK 1 ###
    task_num = 1
    monkey_business = calculate_monkey_business_level(task_num)

    ### TASK 2 ###
    task_num = 2
    monkey_business = calculate_monkey_business_level(task_num)