class Gear:
    def __init__(self, line, column, idx):
        self.coodrinates = (line, column)
        self.gear = idx
        self.neighbors = {
            'top': None,
            'bottom': None,
            'top_left': None, 
            'top_right': None,
            'bottom_left': None,
            'bottom_right': None,
            'left': None,
            'right': None
        }

gear = Gear(1, 3, 0)
gear.neighbors = {
    'top': None,
    'bottom': 5,
    'top_left': 7, 
    'top_right': None,
    'bottom_left': 3,
    'bottom_right': None,
    'left': None,
    'right': None
}

test_schematic = [
    "467..114..",
    "...*......",
    "..35..633.",
    "......#...",
    "617*......",
    ".....+.58.",
    "..592.....",
    "......755.",
    "...$.*....",
    ".664.598.."
]
expected_answer = 467835
expected_test_ratios = [[467, 35], [755, 598]]


# iterate line by line
# for each line, store each gear with its neighbors
# for each gear, get ratio if any

# for a gear's neighbor if digit: complete number