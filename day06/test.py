from solution import solution_part1, solution_part2
    

def test_solution_part1():
    input = ['abcx\nabcy\nabcz']
    
    ret = solution_part1(input)

    assert 6 == ret
    print('test_solution_part1 ... ok')


def test_solution_part2():
    input = ['abcx\nabcy\nabcz']
    
    ret = solution_part2(input)

    assert 3 == ret
    print('test_solution_part2 ... ok')

if __name__ == '__main__':
    test_solution_part1()
    test_solution_part2()

