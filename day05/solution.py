def find_row(row_address):
    """
    Returns row number or None if invalid row_address given.
    """
    rows = range(128)
    half = int(len(rows) / 2)
    # print(len(rows), half)
    
    for a in row_address[:-1]:
        # print(a)
        if a == 'F':
            rows = rows[:half]
        elif a == 'B':
            rows = rows[half:]
        else:
            return None
        
        half = int(len(rows) / 2)
        # print(rows, half)
    
    if len(rows) != 2:
        return None
    
    if row_address[-1] == 'F':
        return rows[0]
    elif row_address[-1] == 'B':
        return rows[1]

    return None

    
def find_column(col_address):
    """
    Returns column number or None if invalid row_address given.
    """
    columns = range(8)
    half = int(len(columns) / 2)
    # print(len(columns), half)
    for a in col_address[:-1]:
        # print(a)
    
        if a == 'L':
            columns = columns[:half]
        elif a == 'R':
            columns = columns[half:]
        else:
            return None
        
        half = int(len(columns) / 2)
        # print(columns, half)
    
    if len(columns) != 2:
        return None
    
    if col_address[-1] == 'L':
        return columns[0]
    elif col_address[-1] == 'R':
        return columns[1]

    return None


def find_seat(ticket):
    # print(ticket)
    row_address = ticket[:7]
    col_address = ticket[7:]
    row = find_row(row_address)
    column = find_column(col_address)
    # print(f'Row: {row}')
    # print(f'Column: {column}')
    return row, column


def calc_seat_id(row, column):
    return row * 8 + column


def solution_part1(input):
    max_seat_id = 0
    for ticket in input:
        row, column = find_seat(ticket.strip())
        if row is None or column is None:
            print(f'WARNING: Invalid ticket {ticket} produced row {row} and column {column}.')
            continue
    
        seat_id = calc_seat_id(row, column)
        if seat_id > max_seat_id:
            max_seat_id = seat_id
    
    return max_seat_id


def solution_part2(input):
    seat_ids = []
    
    for ticket in input:
        row, column = find_seat(ticket.strip())
        if row is None or column is None:
            print(f'WARNING: Invalid ticket {ticket} produced row {row} and column {column}.')
            continue
    
        seat_id = calc_seat_id(row, column)
        seat_ids.append(seat_id)
    
    seat_ids.sort()
    
    previous_seat_id = seat_ids[0]
    
    for seat_id in seat_ids[1:]:
        difference = seat_id - previous_seat_id
        
        if difference > 1:
            return previous_seat_id + 1

        previous_seat_id = seat_id


if __name__ == '__main__':
    with open('input.txt') as f:
        input = f.readlines()

    print('Part 1:')
    
    answer1 = solution_part1(input)
    
    print(f'The answer is: {answer1}')
    
    print('Part 2:')
    
    answer2 = solution_part2(input)
    
    print(f'The answer is: {answer2}')

