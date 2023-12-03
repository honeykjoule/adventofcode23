from typing import List, Tuple

file = open('day02/input.txt', 'r')

MAP = {
    'red': 12,
    'green': 13,
    'blue': 14
}

def get_game_number(line: str) -> int:
    return int(line.split(':')[0].split(' ')[1])

def get_sets(line: str) -> List[str]:
    return line.split(':')[1].split(';')

def get_cubes(set: str) -> List[Tuple[int, str]]:
    cubes = [cube.strip() for cube in set.split(',')]
    return [(int(cube.split(' ')[0]), cube.split(' ')[1]) for cube in cubes]

def is_game_possible(cubes: List[str]) -> bool:
    for count, color in cubes:
        if count > MAP[color]:
            return False
    return True

total = 0
for line in file:
    for set in get_sets(line):
        cubes = get_cubes(set)
        if not is_game_possible(cubes):
            break
    else:
        total += get_game_number(line)
print(total)