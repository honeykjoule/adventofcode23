from typing import List, Tuple

def main():
    file = open('day02/input.txt', 'r')
    total = 0
    for line in file:
        power = get_power(line)
        total += power
    return total

def get_power(line) -> int:
    max_counts = {
        'red': 0,
        'green': 0,
        'blue': 0
    }
    sets = get_sets(line)
    for set in sets:
        cubes = get_cubes(set)
        for count, cube_color in cubes:
            if count > max_counts[cube_color]:
                max_counts[cube_color] = count
    return max_counts['red'] * max_counts['green'] * max_counts['blue']

def get_sets(line):
    return line.split(':')[1].split(';')

def get_cubes(set: str) -> List[Tuple[int, str]]:
    cubes = [cube.strip() for cube in set.split(',')]
    return [(int(cube.split(' ')[0]), cube.split(' ')[1]) for cube in cubes]

if __name__ == '__main__':
    print(main())