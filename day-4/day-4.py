import re
passports_raw = open('input.txt').read().split('\n\n')


def dictify(passport):
    passport = passport.replace('\n', ' ')
    passport = passport.split(' ')
    return dict(item.split(':') for item in passport)


passports = [dictify(passport_raw) for passport_raw in passports_raw]


def verify_required_fields(passport):
    required_fields = ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid')
    for requirement in required_fields:
        if requirement not in passport:
            return False
    return True


def verify_byr(byr):
    if (len(byr) == 4) and (byr.isdigit()) and (int(byr) >= 1920) and (int(byr) <= 2002):
        return True
    else:
        return False


def verify_iyr(iyr):
    if (len(iyr) == 4) and (iyr.isdigit()) and (int(iyr) >= 2010) and (int(iyr) <= 2020):
        return True
    else:
        return False


def verify_eyr(eyr):
    if (len(eyr) == 4) and (eyr.isdigit()) and (int(eyr) >= 2020) and (int(eyr) <= 2030):
        return True
    else:
        return False


def verify_hgt(hgt):
    unit = hgt[-2:]
    size = hgt[:-2]
    if not size.isdigit():
        return False
    else:
        size = int(size)

    if (unit == 'cm') and (size >= 150) and (size <= 193):
        return True
    elif (unit == 'in') and (size >= 59) and (size <= 76):
        return True
    else:
        return False


def verify_hcl(hcl):
    if re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', hcl):
        return True
    else:
        return False


def verify_ecl(ecl):
    valid_colors = ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth')
    if ecl in valid_colors:
        return True
    else:
        return False


def verify_pid(pid):
    if (len(pid) == 9) and (pid.isdigit()):
        return True
    else:
        return False


def verify_passport(passport):
    if not verify_required_fields(passport):
        return False
    if not verify_byr(passport.get('byr')):
        return False
    if not verify_iyr(passport.get('iyr')):
        return False
    if not verify_eyr(passport.get('eyr')):
        return False
    if not verify_hgt(passport.get('hgt')):
        return False
    if not verify_hcl(passport.get('hcl')):
        return False
    if not verify_ecl(passport.get('ecl')):
        return False
    if not verify_pid(passport.get('pid')):
        return False
    return True


def part_one(passports):
    print('## Part One ##')
    valid = invalid = 0
    for passport in passports:
        if verify_required_fields(passport):
            valid = valid + 1
        else:
            invalid = invalid + 1

    print(f'Valid passports: {valid}\nInvalid passports: {invalid} \n')


def part_two(passports):
    print('## Part Two ##')
    valid = invalid = 0
    for passport in passports:
        if verify_passport(passport):
            valid = valid + 1
        else:
            invalid = invalid + 1

    print(f'Valid passports: {valid}\nInvalid passports: {invalid} \n')


# Part 1
part_one(passports)

# Part 2
part_two(passports)