from collections import namedtuple


InnerBag = namedtuple('InnerBag', ['num', 'color'])


def get_all_children(color, rules):
    children = []
    if color in rules:
        print('yes')
        for child in rules[color]:
            children.append(child)
            children += get_all_children(child, rules)
    return children


def solution_part1(input):
    rules = {}
    
    for rule in input:
        try:
            outer_bag, inner_bags_str = rule.split('contain')
        except:
            print(f'WARNING: bad rule "{rule}".')
        
        outer_bag_color = outer_bag.strip(' bags')
        # print(f'Outer Bag Color: "{outer_bag_color}"')
        inner_bags = []
        
        for ibag in inner_bags_str.strip('.').split(','):
            ibag = ibag.strip().strip(' bags')
            num = ibag[0]
            if num == 'n':
                continue
            num = int(num)
            color = ibag[2:]
            # print(f'Num: "{num}" Color: "{color}"')
            inner_bags.append(InnerBag(num, color))
        
        # print(inner_bags)
        
        if outer_bag_color in rules:
            # print(f'Duplicate Outer Bag Color: {outer_bag_color}')
            rules[outer_bag_color] += inner_bags
        else:
            rules[outer_bag_color] = inner_bags
    
    for color in rules:
        all_children = get_all_children(color, rules)
        print(color)
        print(len(all_children))
    
    # for outer_bag, inner_bags in rules.items():
    #    print(outer_bag)
    #    print(inner_bags)
            
            
            
        


def solution_part2(input):
    pass

if __name__ == '__main__':
    with open('input.txt') as f:
        input = f.read().split('\n')

    print('Part 1:')
    
    answer1 = solution_part1(input)
    
    print(f'The answer is: {answer1}')
    
    print('Part 2:')
    
    answer2 = solution_part2(input)
    
    print(f'The answer is: {answer2}')

