file = open('day01/input.txt', 'r')

# Part 1
sum = 0
for line in file:
    first_digit = None
    last_digit = None

    for char in line:
        if char.isdigit():
            first_digit = char
            break
    for char in reversed(line):
        if char.isdigit():
            last_digit = char
            break
    if first_digit is not None and last_digit is not None:
        sum += int(first_digit + last_digit)

print(sum)