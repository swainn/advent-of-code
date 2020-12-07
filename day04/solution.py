import re


def parse_passport_batch(input):
    raw_passports = input.split('\n\n')
    passports =[]
    for p in raw_passports:
        field_dict = {}
        fields = p.split()
        for field in fields:
            field, val = field.split(':')
            field_dict.update({field: val})
        passports.append(field_dict)
    return passports


def validate_passports(passports, validate_fields=False):
    """
    byr (Birth Year) - four digits; at least 1920 and at most 2002.
    iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    hgt (Height) - a number followed by either cm or in:
    If cm, the number must be at least 150 and at most 193.
    If in, the number must be at least 59 and at most 76.
    hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    pid (Passport ID) - a nine-digit number, including leading zeroes.
    cid (Country ID) - ignored, missing or not.
    """
    num_valid = 0
    hgt_prog = re.compile('^(?P<number>[0-9]{1,3})(?P<units>cm|in)$')
    hcl_prog = re.compile('^#[0-9a-f]{6}$')
    pid_prog = re.compile('^[0-9]{9}$')
    
    for passport in passports:
        byr = passport.get('byr')
        iyr = passport.get('iyr')
        eyr = passport.get('eyr')
        hgt = passport.get('hgt')
        hcl = passport.get('hcl')
        ecl = passport.get('ecl')
        pid = passport.get('pid')
        
        if not byr or not iyr or not eyr or not hgt or not hcl or not ecl or not pid:
            # print(f'Passport missing field: {", ".join(list(passport.keys()))}')
            continue
        
        if validate_fields:
            # byr
            if len(byr) != 4 or int(byr) < 1920 or int(byr) > 2002:
                # print(f'Invalid byr: {byr}')
                continue
            
            # iyr
            if len(iyr) != 4 or int(iyr) < 2010 or int(iyr) > 2020:
                # print(f'Invalid iyr: {iyr}')
                continue
            
            # eyr
            if len(eyr) != 4 or int(eyr) < 2020 or int(eyr) > 2030:
                # print(f'Invalid eyr: {eyr}')
                continue
            
            # hgt
            hgt_match = hgt_prog.match(hgt)
            if not hgt_match:
                # print(f'Invalid hgt: {hgt}')
                continue
            
            hgt_number = float(hgt_match.group('number'))
            hgt_units = hgt_match.group('units')
            
            if hgt_units == 'in' and (hgt_number < 59 or hgt_number > 76):
                # print(f'Invalid hgt: {hgt}')
                continue
            
            elif hgt_units == 'cm' and (hgt_number < 150 or hgt_number > 193):
                # print(f'Invalid hgt: {hgt}')
                continue
 
            # hcl
            if not hcl_prog.match(hcl):
                # print(f'Invalid hcl: {hcl}')
                continue
            
            # ecl
            if ecl not in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'):
                # print(f'Invalid ecl: {ecl}')
                continue
            
            # pid
            if not pid_prog.match(pid):
                # print(f'Invalid pid: {pid}')
                continue

        num_valid += 1
        
    return num_valid


def solution_part1(input):
    passports = parse_passport_batch(input)
    return validate_passports(passports)


def solution_part2(input):
    passports = parse_passport_batch(input)
    return validate_passports(passports, validate_fields=True)

if __name__ == '__main__':
    with open('input.txt') as f:
        input = f.read()

    print('Part 1:')
    
    answer1 = solution_part1(input)
    
    print(f'The answer is: {answer1}')
    
    print('Part 2:')
    
    answer2 = solution_part2(input)
    
    print(f'The answer is: {answer2}')

