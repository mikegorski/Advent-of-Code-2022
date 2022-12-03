def load_input(filename):
    with open(filename) as input_file:
        input = [line.rstrip('\n') for line in input_file]
        input = [int(x) if x != '' else 0 for x in input]
        return input

def return_total_list(list):
    total = 0
    total_list = []
    for value in list:
        if value != 0:
            total += value
        else:
            total_list.append(total)
            total = 0
    total_list.append(total)
    total_list.sort(reverse=True)
    return total_list

kcal_list = load_input('data.txt')
total_kcal_list = return_total_list(kcal_list)
top_value = total_kcal_list[0]
top3_values_sum = sum(total_kcal_list[0:3])
print(f'Highest total calory value is {top_value}')
print(f'Sum of 3 highest total calory values is {top3_values_sum}')