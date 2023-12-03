file = open('day01/input.txt', 'r')

# Part 2
MAP = {
    'zero': '0',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}


def calculate_sum_from_lines(file):
    total_sum = 0

    for line in file:
        first_digit = None
        last_digit = None
        first_digit_index = len(line)  # Initialize to max length
        last_digit_index = -1         # Initialize to -1

        # Find the first digit or number word
        for i, char in enumerate(line):
            if char.isdigit() and first_digit_index == len(line):
                first_digit = char
                first_digit_index = i
                break

        for i in range(len(line)):
            for j in range(i + 1, len(line) + 1):
                if line[i:j] in MAP:
                    if i < first_digit_index:
                        first_digit_index = i
                        first_digit = MAP[line[i:j]]
                    break

        # Find the last digit or number word
        for i in range(len(line) - 1, -1, -1):
            if line[i].isdigit() and last_digit_index == -1:
                last_digit_index = i
                last_digit = line[i]
                break

        for i in range(len(line) - 1, -1, -1):
            for j in range(i, -1, -1):
                if line[j:i + 1] in MAP:
                    if i > last_digit_index:
                        last_digit_index = i
                        last_digit = MAP[line[j:i + 1]]
                        break

        # Add to the total sum if both digits are found
        if first_digit is not None and last_digit is not None:
            total_sum += int(first_digit + last_digit)

    return total_sum

sum = calculate_sum_from_lines(file)
print(sum)