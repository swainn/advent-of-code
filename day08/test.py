from solution import solution_part1, solution_part2
    

def test_solution_part1():
    input = ['nop +0',
             'acc +1',
             'jmp +4',
             'acc +3',
             'jmp -3',
             'acc -99',
             'acc +1',
             'jmp -4',
             'acc +6']
    
    ret = solution_part1(input)

    assert 5 == ret
    print('test_solution_part1 ... ok')


def test_solution_part2():
    input = ['nop +0',
             'acc +1',
             'jmp +4',
             'acc +3',
             'jmp -3',
             'acc -99',
             'acc +1',
             'jmp -4',
             'acc +6']
    
    ret = solution_part2(input)

    assert 8 == ret
    print('test_solution_part2 ... ok')

if __name__ == '__main__':
    test_solution_part1()
    test_solution_part2()

