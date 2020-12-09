import string


def count_yes_questions(group):
    yes_answers = set()
    for person in group:
        for q in person:
            yes_answers.add(q)
    
    return len(yes_answers)

def count_common_yes(group):
    all_yes = set(list(string.ascii_lowercase))
    # print(group)
    for person in group:
        person_set = set(list(person))
        all_yes = all_yes.intersection(person_set)
    
    # print(all_yes)
    return(len(all_yes))
    
    
    
def solution_part1(input):
    total = 0
    for group in input:
        total += count_yes_questions(group.split())

    return total


def solution_part2(input):
    total = 0
    for group in input:
        total += count_common_yes(group.split())

    return total

if __name__ == '__main__':
    with open('input.txt') as f:
        input = f.read().split('\n\n')

    print('Part 1:')
    
    answer1 = solution_part1(input)
    
    print(f'The answer is: {answer1}')
    
    print('Part 2:')
    
    answer2 = solution_part2(input)
    
    print(f'The answer is: {answer2}')

