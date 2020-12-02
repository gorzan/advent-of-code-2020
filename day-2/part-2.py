passwords = open('input.txt').read().split('\n')
passwords = [tuple(i.split(': ')) for i in passwords]


def verify_password(rule, password):
    pos_1 = int(rule.split('-')[0]) - 1
    pos_2 = int(rule.split('-')[1].split(' ')[0]) - 1
    char = rule.split(' ')[1]
    if ((password[pos_1] == char) or (password[pos_2] == char)) and (password[pos_1] != password[pos_2]):
        return True
    else:
        return False


valid = invalid = 0

for password in passwords:
    print(f'Rule: {password[0]}   Password: {password[1]}   Result: {verify_password(*password)}')
    if verify_password(*password):
        valid = valid + 1
    else:
        invalid = invalid + 1

print(f'Valid passwords: {valid}, invalid passwords: {invalid}')