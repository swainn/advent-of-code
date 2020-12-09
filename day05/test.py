from solution import find_seat, calc_seat_id, solution_part1


def test_find_seat():
    """
    BFFFBBFRRR: row 70, column 7, seat ID 567.
    FFFBBBFRRR: row 14, column 7, seat ID 119.
    BBFFBBFRLL: row 102, column 4, seat ID 820.
    """
    ticket = 'BFFFBBFRRR'
    row, column = find_seat(ticket)
    seat_id = calc_seat_id(row, column)
    assert 70 == row
    assert 7 == column
    assert 567 == seat_id
    
    ticket = 'FFFBBBFRRR'
    row, column = find_seat(ticket)
    seat_id = calc_seat_id(row, column)
    assert 14 == row
    assert 7 == column
    assert 119 == seat_id
    
    ticket = 'BBFFBBFRLL'
    row, column = find_seat(ticket)
    seat_id = calc_seat_id(row, column)
    assert 102 == row
    assert 4 == column
    assert 820 == seat_id
    
    print('test_find_seat ... ok')

def test_solution_part1():
    input = ['BFFFBBFRRR\n', 'FFFBBBFRRR\n', 'BBFFBBFRLL']
    
    ret = solution_part1(input)
    
    assert 820 == ret
    print('test_solution_part1 ... ok')

if __name__ == '__main__':
    test_find_seat()
    test_solution_part1()

