from solution import solution

def test_2_2020():
    input = [1721, 979, 366, 299, 675, 1456]
    
    ret = solution(input, 2020, 2)
    
    assert 514579 == ret
    print(f'Tests succeeded: 514579 == {ret}')


def test_3_2020():
    input = [1721, 979, 366, 299, 675, 1456]
    
    ret = solution(input, 2020, 3)
    
    assert 241861950 == ret
    print(f'Tests succeeded: 241861950 == {ret}')


if __name__ == '__main__':
    test_2_2020()
    test_3_2020()
