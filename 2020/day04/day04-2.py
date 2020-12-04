import re


def passport_to_dict(list_of_key_value_pair_strings):
    return dict((key, value) for key, value in (element.split(':') for element in list_of_key_value_pair_strings))


def check_fields(passport_dict):
    try:
        birth_year = int(passport_dict['byr'])
    except ValueError:
        return False
    if birth_year < 1920 or birth_year > 2002:
        return False

    try:
        issue_year = int(passport_dict['iyr'])
    except ValueError:
        return False
    if issue_year < 2010 or issue_year > 2020:
        return False

    try:
        expiration_year = int(passport_dict['eyr'])
    except ValueError:
        return False
    if expiration_year < 2020 or expiration_year > 2030:
        return False

    try:
        height = int(passport_dict['hgt'][:-2])
    except ValueError:
        return False
    if passport_dict['hgt'].endswith('cm'):
        if height < 150 or height > 193:
            return False
    elif passport_dict['hgt'].endswith('in'):
        if height < 59 or height > 76:
            return False
    else:
        return False

    if not re.fullmatch(r'#[0-9a-f]{6}', passport_dict['hcl']):
        return False

    if passport_dict['ecl'] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        return False

    if not re.fullmatch(r'[0-9]{9}', passport_dict['pid']):
        return False

    return True


with open('puzzle4-data', 'r') as f:
    data = [passport.split() for passport in f.read().split('\n\n')]

passports = [passport_to_dict(passport) for passport in data]

count = 0
expected_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
for passport in passports:
    required_fields_present = True
    for field in expected_fields:
        if field not in passport:
            required_fields_present = False
            break
    if required_fields_present:
        if check_fields(passport):
            count += 1

print(count)
