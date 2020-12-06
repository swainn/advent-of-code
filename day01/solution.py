import itertools
import math
from pprint import pprint


def solution(input, target, num_to_combine=2):
    
    for numbers in itertools.combinations(input, num_to_combine):
        
        sum = 0
        for n in numbers:
            sum += n
   
        if sum == target:
            product = 1
            for m in numbers:
                product = product * m
            return product
        
    return None


if __name__ == '__main__':
    with open('input.txt') as f:
        lines = f.readlines()
    
    input = [int(num) for num in lines]
       
    print('Part 1:')
    answer1 = solution(input, 2020)
    print(f'The answer is: {answer1}')
    
    print('Part 2:')
    answer2 = solution(input, 2020, 3)
    print(f'The answer is: {answer2}')
