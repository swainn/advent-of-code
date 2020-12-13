import copy
from itertools import combinations


def count_diffs(input):
    input.sort()
    # Add 0 joltage at beginning
    input.insert(0, 0)
    # Add device 3 jolt max adapter
    input.append(input[-1] + 3)
    # print(input)
    idx_1 = 0
    idx_2 = 1
    diff_of_1 = 0
    diff_of_3 = 0

    while idx_2 < len(input):
        diff = input[idx_2] - input[idx_1]
        #print(diff)
        if diff == 1:
            diff_of_1 += 1
        elif diff == 3:
            diff_of_3 += 1
        elif diff > 3:
            # print(f'WARNING: Joltage difference too large: {diff}')
            return None
        idx_1 += 1
        idx_2 += 1
    
    # print(diff_of_1, diff_of_3)
    # print(input)
    answer = diff_of_1 * diff_of_3
    return answer


def valid_arrangment(input, max_needed):
    input.sort()
    # Add 0 joltage at beginning
    input.insert(0, 0)
    # Add device 3 jolt max adapter
    input.append(max_needed)
    
    idx_1 = 0
    idx_2 = 1
    diff_of_1 = 0
    diff_of_3 = 0

    while idx_2 < len(input):
        diff = input[idx_2] - input[idx_1]
        #print(diff)
        if diff > 3 or diff == 0:
            # print(f'WARNING: Joltage difference too large: {diff}')
            return False
        idx_1 += 1
        idx_2 += 1
    
    # print(diff_of_1, diff_of_3)
    # print(input)
    return True


def solution_part1(input):
    return count_diffs(copy.deepcopy(input))


def solution_part2(input):
    num_valid_combinations = 0
    len_of_sets = len(input)
    input.sort()
    max_needed = input[-1] + 3
    # print(max_needed)
    
    while len_of_sets > 0:
        combos = combinations(input, len_of_sets)
        for combo in combos:
            # print(combo)
            valid = valid_arrangment(list(combo), max_needed)
            if valid:
                num_valid_combinations += 1
        
        len_of_sets -= 1
        # print(len_of_sets)
    
    return num_valid_combinations
    


if __name__ == '__main__':
    with open('input.txt') as f:
        parsed = f.readlines()
    
    input = []
    for line in parsed:
        input.append(int(line.strip()))

    print('Part 1:')
    
    answer1 = solution_part1(input)
    
    print(f'The answer is: {answer1}')
    
    print('Part 2:')
    
    answer2 = solution_part2(input)
    
    print(f'The answer is: {answer2}')

