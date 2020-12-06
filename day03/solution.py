import copy


class Grid:
    tree = '#'
    
    def __init__(self, input):
        self.rows = []
        for line in input:
            row = list(line.strip())
            self.rows.append(row)
    
    def get_cell_val(self, x, y):
        """
        Positive directions. x is column and y is the row.
        0,0 ========>
        ||
        ||
        ||
        \/
        """
        try:
            row = self.rows[y]
        except IndexError:
            return None
        
        cell_val = row[x % len(row)]
        # print(x % len(row))
        # print(cell_val)
        return cell_val
    
    def trees_for_slope(self, right, down):
        num_trees = 0
        
        # Get initial val
        x = 0
        y = 0
        val = self.get_cell_val(x, y)
        
        while val is not None:
            # Check for tree
            if val == self.tree:
                num_trees += 1
                
            # Get next val
            x += right
            y += down
            val = self.get_cell_val(x, y)
        
        return num_trees


def solution_part1(input):
    grid = Grid(input)
    num_trees = grid.trees_for_slope(3, 1)
    return num_trees
        


def solution_part2(input):
    """
    Right 1, down 1.
    Right 3, down 1. (This is the slope you already checked.)
    Right 5, down 1.
    Right 7, down 1.
    Right 1, down 2.
    2, 7, 3, 4, and 2, respectively.
    """
    grid = Grid(input)
    
    num_trees_11 = grid.trees_for_slope(1, 1)
    num_trees_31 = grid.trees_for_slope(3, 1)
    num_trees_51 = grid.trees_for_slope(5, 1)
    num_trees_71 = grid.trees_for_slope(7, 1)
    num_trees_12 = grid.trees_for_slope(1, 2)
    # print(num_trees_11, num_trees_31, num_trees_51, num_trees_71, num_trees_12)
    
    product = num_trees_11 * num_trees_31 * num_trees_51 * num_trees_71 * num_trees_12
    return product
    


if __name__ == '__main__':
    with open('input.txt') as f:
        input = f.readlines()

    print('Part 1:')
    
    answer1 = solution_part1(input)
    
    print(f'The answer is: {answer1}')
    
    print('Part 2:')
    
    answer2 = solution_part2(input)
    
    print(f'The answer is: {answer2}')

