from solution import solution_part1, solution_part2
    

def test_solution_part1():
    input = [35, 20, 15, 25, 47, 40, 62, 55, 65, 95, 102, 117, 150, 182, 127, 219, 299, 277, 309, 576]
    
    ret = solution_part1(input, 5)

    assert 127 == ret
    print('test_solution_part1 ... ok')


def test_solution_part2():
    input = [35, 20, 15, 25, 47, 40, 62, 55, 65, 95, 102, 117, 150, 182, 127, 219, 299, 277, 309, 576]
    
    ret = solution_part2(input, 5)

    assert 62 == ret
    print('test_solution_part2 ... ok')

if __name__ == '__main__':
    test_solution_part1()
    test_solution_part2()

