def parse_input(filename):
    with open(filename) as f:
        input = [eval(line.rstrip('\n')) for line in f]
    return input

def is_adjacent(c1, c2):
    if abs(c1[0] - c2[0]) == 1 and c1[1] == c2[1] and c1[2] == c2[2]:
        return True
    elif c1[0] == c2[0] and abs(c1[1] - c2[1]) == 1 and c1[2] == c2[2]:
        return True
    elif c1[0] == c2[0] and c1[1] == c2[1] and abs(c1[2] - c2[2]) == 1:
        return True
    else:
        return False

def count_free_sides(cubes):
    surface_area = len(cubes) * 6
    for i in range(len(cubes) - 1):
        for j in range(i+1, len(cubes)):
            if is_adjacent(cubes[i], cubes[j]):
                surface_area -= 2
    return surface_area

def get_air_pocket_outer_surface_area(cubes):
    x_min, y_min, z_min = cubes[0]
    x_max, y_max, z_max = cubes[0]
    for cube in cubes:
        x_min = min(x_min, cube[0])
        y_min = min(y_min, cube[1])
        z_min = min(z_min, cube[2])
        x_max = max(x_max, cube[0])
        y_max = max(y_max, cube[1])
        z_max = max(z_max, cube[2])    
    min_coord = min(x_min, y_min, z_min)
    max_coord = max(x_max, y_max, z_max)

    air_cubes = []
    for x in range(min_coord, max_coord + 1):
        for y in range(min_coord, max_coord + 1):
            for z in range(min_coord, max_coord + 1):
                if (x, y, z) not in cubes:
                    air_cubes.append((x, y, z))
    
    air_pocket_outer_surface = 0
    while air_cubes:
        adjacent = list()
        air_pocket = True
        adjacent.append(air_cubes[0])
        for adj in adjacent:
            x, y, z = adj
            neighbours = [(x-1,y,z), (x+1,y,z),
                        (x,y-1,z), (x,y+1,z),
                        (x,y,z-1), (x,y,z+1)]
            neighbours = [i for i in neighbours if i in air_cubes and i not in adjacent]
            for neighbour in neighbours:
                if neighbour[0] == x_min or neighbour[0] == x_max\
                   or neighbour[1] == y_min or neighbour[1] == y_max\
                   or neighbour[2] == z_min or neighbour[2] == z_max:
                    air_pocket = False
                    break
            for neighbour in neighbours:
                adjacent.append(neighbour)
        if air_pocket:
            air_pocket_outer_surface += count_free_sides(adjacent)
        air_cubes = list(set(air_cubes).difference(set(adjacent)))
    return air_pocket_outer_surface


if __name__ == "__main__":

    ### TASK 1 ###
    cubes = parse_input('data.txt')
    free_surface_area = count_free_sides(cubes)
    print(f'Total free surface area is {free_surface_area}.')

    ### TASK 2 ###
    cubes = parse_input('data.txt')
    free_surface_area = count_free_sides(cubes)
    air_pocket_outer_surface = get_air_pocket_outer_surface_area(cubes)
    free_outer_surface_area = free_surface_area - air_pocket_outer_surface
    print(f'Total free outer surface area is {free_outer_surface_area}.')