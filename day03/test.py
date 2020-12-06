from solution import solution_part1, solution_part2


def test_solution_part1():
    input = [
        '..##.......\n',
        '#...#...#..\n',
        '.#....#..#.\n',
        '..#.#...#.#\n',
        '.#...##..#.\n',
        '..#.##.....\n',
        '.#.#.#....#\n',
        '.#........#\n',
        '#.##...#...\n',
        '#...##....#\n',
        '.#..#...#.#\n'
    ]
    
    ret = solution_part1(input)
    print(ret)
    assert 7 == ret
    print(f'Test succeeded: 7 == {ret}')

def test_solution_part2():
    input = [
        '..##.......\n',
        '#...#...#..\n',
        '.#....#..#.\n',
        '..#.#...#.#\n',
        '.#...##..#.\n',
        '..#.##.....\n',
        '.#.#.#....#\n',
        '.#........#\n',
        '#.##...#...\n',
        '#...##....#\n',
        '.#..#...#.#\n'
    ]
    
    ret = solution_part2(input)
    print(ret)
    assert 336 == ret
    print(f'Test succeeded: 336 == {ret}')

if __name__ == '__main__':
    test_solution_part1()
    test_solution_part2()

