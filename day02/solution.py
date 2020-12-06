def parse_line(line):
    counts, letter, password = line.split(' ')
    num1, num2 = counts.split('-')
    letter = letter.replace(':', '')
    return password, int(num1), int(num2), letter


def solution_part1(input):
    num_valid = 0
    
    for line in input:
        password, min, max, letter = parse_line(line)
        
        # print(f'min: {min}, max: {max}, letter: {letter}, password: {password}')
        
        num_occurances = password.count(letter)
        
        # print(num_occurances)
        
        if num_occurances >= min and num_occurances <= max:
            num_valid += 1
    
    return num_valid


def solution_part2(input):
    num_valid = 0

    for line in input:
        password, position1, position2, letter = parse_line(line)
        
        at_position1 = password[position1 - 1] == letter
        at_position2 = password[position2 - 1] == letter
        
        # print(at_position1, at_position2)
        
        if at_position1 and not at_position2:
            num_valid += 1
        elif not at_position1 and at_position2:
            num_valid += 1

    return num_valid


if __name__ == '__main__':
    with open('input.txt') as f:
        input = f.readlines()

    print('Part 1:')
    
    answer1 = solution_part1(input)
    
    print(f'The answer is: {answer1}')
    
    print('Part 2:')
    
    answer2 = solution_part2(input)
    
    print(f'The answer is: {answer2}')

