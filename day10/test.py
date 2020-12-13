from solution import solution_part1, solution_part2
    

def test_solution_part1_example1():
    input = [16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4]
    
    ret = solution_part1(input)

    assert 35 == ret
    print('test_solution_part1_example1 ... ok')


def test_solution_part1_example2():
    input = [28, 33, 18, 42, 31, 14, 46, 20, 48, 47,
             24, 23, 49, 45, 19, 38, 39, 11, 1, 32, 
             25, 35, 8, 17, 7, 9, 4, 2, 34, 10, 3]
    
    ret = solution_part1(input)

    assert 220 == ret
    print('test_solution_part1_example2 ... ok')


def test_solution_part2_example1():
    input = [16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4]
    
    ret = solution_part2(input)

    assert 8 == ret
    print('test_solution_part2_example1 ... ok')


def test_solution_part2_example2():
    input = [28, 33, 18, 42, 31, 14, 46, 20, 48, 47,
             24, 23, 49, 45, 19, 38, 39, 11, 1, 32, 
             25, 35, 8, 17, 7, 9, 4, 2, 34, 10, 3]
    
    ret = solution_part2(input)

    assert 19208 == ret
    print('test_solution_part2_example2 ... ok')

if __name__ == '__main__':
    test_solution_part1_example1()
    test_solution_part1_example2()
    test_solution_part2_example1()
    test_solution_part2_example2()

