from itertools import combinations

def compute_valid_next_numbers(preamble):
    # print(preamble)
    # print(len(preamble))
    valid_numbers = []
    all_combinations = combinations(preamble, 2)
    for combo in all_combinations:
        # print(combo)
        valid_numbers.append(sum(combo))
    # print(valid_numbers)
    return valid_numbers


def find_invalid_number(input, len_preamble):
    preamble_start = 0
    preamble_end = len_preamble
    next_number_index = len_preamble
    # print(input)
    
    while next_number_index < len(input):
        valid_numbers = compute_valid_next_numbers(input[preamble_start:preamble_end])
        next_number = input[next_number_index]
        if next_number not in valid_numbers:
            # print(f'INVALID NUMBER: {next_number}')
            return next_number
        preamble_start += 1
        preamble_end += 1
        next_number_index += 1


def solution_part1(input, len_preamble):
    return find_invalid_number(input, len_preamble)


def solution_part2(input, len_preamble):
    invalid_number = find_invalid_number(input, len_preamble)
    the_range = None
    len_sum_range = 2
    
    while len_sum_range <= len(input):
        # print(f'Testing sums of {len_sum_range}...')
        curr_range_begin = 0
        curr_range_end = 2
        
        while curr_range_end != len(input):
            curr_range_end = curr_range_begin + len_sum_range
            curr_range = input[curr_range_begin:curr_range_end]
            range_sum = sum(curr_range)
            
            # print(range_sum)
            
            if range_sum == invalid_number:
                # print(sum(curr_range))
                # print(curr_range)
                the_range = curr_range
                break
            
            curr_range_begin += 1
        
        if the_range is not None:
            break
        
        len_sum_range += 1
    
    if the_range is not None:
        return min(the_range) + max(the_range)


if __name__ == '__main__':
    with open('input.txt') as f:
        parsed = f.readlines()
    
    input = []
    for line in parsed:
        input.append(int(line.strip()))

    print('Part 1:')
    
    answer1 = solution_part1(input, 25)
    
    print(f'The answer is: {answer1}')
    
    print('Part 2:')
    
    answer2 = solution_part2(input, 25)
    
    print(f'The answer is: {answer2}')

