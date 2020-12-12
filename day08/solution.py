import copy


def solution_part1(input):
    accumulator = 0
    instructions_run = []
    next_instruction = 0
    num_instructions = len(input)
    
    while True:
        curr_instruction = next_instruction
        try:
            command, argument = input[curr_instruction].split()
        except IndexError:
            print(f'{curr_instruction} not in {num_instructions}')
            print('END OF EXECUTION REACHED')
            break
        
        if curr_instruction in instructions_run:
            # print('SECOND TIME')
            break
        
        if command == "nop":
            next_instruction += 1
        elif command == "acc":
            accumulator += int(argument)
            next_instruction += 1
        elif command == "jmp":
            next_instruction += int(argument)
        else:
            print('WARNING: Invalid command')
        
        instructions_run.append(curr_instruction)
        # print(command, int(argument))
    
    return accumulator

def run_program(input):
    accumulator = 0
    instructions_run = []
    next_instruction = 0
    num_instructions = len(input)
    
    while True:
        curr_instruction = next_instruction
        try:
            command, argument = input[curr_instruction].split()
        except IndexError:
            # print(f'{curr_instruction} not in {num_instructions - 1}')
            # print('END OF EXECUTION REACHED')
            break
        
        if curr_instruction in instructions_run:
            # print('INFINITE LOOP DETECTED')
            # print(command, argument)
            return None
        
        if command == "nop":
            next_instruction += 1
        elif command == "acc":
            accumulator += int(argument)
            next_instruction += 1
        elif command == "jmp":
            next_instruction += int(argument)
        else:
            print('WARNING: Invalid command')
        
        instructions_run.append(curr_instruction)
        # print(command, int(argument))
    
    return accumulator

def solution_part2(input):
    jmp_instructions = []
    nop_instructions = []
    accumulator = None
    fixed = False
    
    for idx, instruction in enumerate(input):
        if 'jmp' in instruction:
            jmp_instructions.append(idx)
        elif 'nop' in instruction:
            nop_instructions.append(idx)
    
    for jmp_idx in jmp_instructions:
        curr_input = copy.deepcopy(input)
        curr_jmp = curr_input[jmp_idx]
        new_jmp = curr_jmp.replace('jmp', 'nop')
        # print(f'Changing line {jmp_idx}: "{curr_jmp.strip()}" -> "{new_jmp.strip()}"...')
        curr_input[jmp_idx] = new_jmp
            
        accumulator = run_program(curr_input)
        
        if accumulator is not None:
            break
    
    return accumulator

if __name__ == '__main__':
    with open('input.txt') as f:
        input = f.readlines()

    print('Part 1:')
    
    answer1 = solution_part1(input)
    
    print(f'The answer is: {answer1}')
    
    print('Part 2:')
    
    answer2 = solution_part2(input)
    
    print(f'The answer is: {answer2}')

