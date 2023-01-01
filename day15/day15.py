def parse_input(filename):
    with open(filename) as f:
        input = [line.rstrip('\n').split(':') for line in f]
        sensors = []
        beacons = []
        for line in input:
            sensors.append((int(line[0].split('x=')[1].split(',')[0]), 
                            int(line[0].split('y=')[1])))
            beacons.append((int(line[1].split('x=')[1].split(',')[0]), 
                            int(line[1].split('y=')[1])))
    return sensors, beacons

def dist(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def task1(sensors, beacons):
    target_row = 2000000
    beacon_impossible = set()

    for idx, sensor in enumerate(sensors):
        x_diff = dist(sensor, beacons[idx]) - abs(sensor[1] - target_row)
        for x in range(sensor[0] - x_diff, sensor[0] + x_diff + 1):
            if (x, target_row) not in beacons:
                    beacon_impossible.add(x)
    print(f'For y={target_row}, there are {len(beacon_impossible)}',
           'impossible beacon positions.')

def is_in_bounds(loc, bounds):
    if bounds[0] <= loc[0] <= bounds[1]:
        if bounds[0] <= loc[1] <= bounds[1]:
            return True
        else:
            return False
    return False

def is_covered(loc, sensors, beacons):
    for idx, sensor in enumerate(sensors):
        if dist(loc, sensor) <= dist(sensor, beacons[idx]):
            return True
    return False

def task2(sensors, beacons):
    already_checked = set()
    bounds = (0, 4000000)
    for idx, sensor in enumerate(sensors):
        distance = dist(sensor, beacons[idx]) + 1
        for dx in range(distance + 1):
            dy = distance - dx
            points = []
            points.append((sensor[0] + dx, sensor[1] + dy))
            points.append((sensor[0] - dx, sensor[1] + dy))
            points.append((sensor[0] + dx, sensor[1] - dy))
            points.append((sensor[0] - dx, sensor[1] - dy))
            for p in points:
                if p not in already_checked:
                    if is_in_bounds(p, bounds):
                        if is_covered(p, sensors, beacons):
                            already_checked.add(p)
                        else:
                            return p


if __name__ == "__main__":

    ### TASK 1 ###
    task1(*parse_input('data.txt'))
    
    ### TASK 2 ###
    hiding_loc = task2(*parse_input('data.txt'))
    tuning_freq = hiding_loc[0] * 4000000 + hiding_loc[1]
    print(f'Distress beacon position is {hiding_loc} and its',
          f'tuning frequency is {tuning_freq}.')