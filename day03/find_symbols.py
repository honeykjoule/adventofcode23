def find_symbols():
    hypothetical_symbols = set('*#@$%&+-/')
    symbols_in_file = set()
    with open('day03/input.txt', 'r') as file:
        for line in file:
            for char in line.strip():
                if not char.isdigit() and char != '.':
                    symbols_in_file.add(char)
    extra_symbols = symbols_in_file - hypothetical_symbols
    return extra_symbols

if __name__ == '__main__':
    extra_symbols = find_symbols()
    if extra_symbols:
        print(f'The following symbols are in the file but not in the provided set: {extra_symbols}')
    else:
        print('All symbols in the file are in the provided set.')