import re

def main(schematic=None):
    answer = 0
    if schematic is None:
        with open('day03/input.txt', 'r') as file:
            schematic = [list(line.strip()) for line in file]
    else:
        schematic = [list(line.strip()) for line in schematic]
    for row, line in enumerate(schematic):
        line_str = ''.join(line)
        for match in re.finditer(r'\d+', line_str):
            num = int(match.group())
            col_range = range(*match.span())
            if has_symbol_neighbor(schematic, row, col_range):
                answer += num
    return answer


            
def has_symbol_neighbor(schematic, row, col_range):
    symbols = set('=*#@$%&+-/')
    max_row = len(schematic)
    max_col = len(schematic[0])
    for col in col_range:
        for i in range(max(0, row-1), min(max_row, row+2)):
            for j in range(max(0, col-1), min(max_col, col+2)):
                if (i != row or j != col) and schematic[i][j] in symbols:
                    if schematic[i][j] in symbols:
                        return True
    return False

def test_sum_of_parts():
    schematic = [
        '467..114..',
        '...*......',
        '..35..633.',
        '......#...',
        '617*......',
        '.....+.58.',
        '..592.....',
        '......755.',
        '...$.*....',
        '.664.598..'
    ]
    expected = 4361
    result = main(schematic=schematic)
    assert result == expected, f'Expected {expected}, but got {result}'
    print('Tests passed!')

if __name__ == '__main__':
    print(main())
    #test_sum_of_parts()

