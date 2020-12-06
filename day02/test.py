from solution import solution_part1, solution_part2


def test_solution_part1():
    input = [
        '1-3 a: abcde',
        '1-3 b: cdefg',
        '2-9 c: ccccccccc'
    ]
    
    ret = solution_part1(input)
    
    assert 2 == ret
    print(f'Test succeeded: 2 == {ret}')

def test_solution_part2():
    input = [
        '1-3 a: abcde',
        '1-3 b: cdefg',
        '2-9 c: ccccccccc'
    ]
    
    ret = solution_part2(input)
    
    assert 1 == ret
    print(f'Test succeeded: 1 == {ret}')

if __name__ == '__main__':
    test_solution_part1()
    test_solution_part2()
    
