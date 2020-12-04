def passport_to_dict(list_of_key_value_pair_strings):
    return dict((key, value) for key, value in (element.split(':') for element in list_of_key_value_pair_strings))


with open('puzzle4-data', 'r') as f:
    data = [passport.split() for passport in f.read().split('\n\n')]

passports = [passport_to_dict(passport) for passport in data]

count = 0
expected_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
for passport in passports:
    valid = True
    for field in expected_fields:
        if field not in passport:
            valid = False
            break
    if valid:
        count += 1

print(count)
