passwords = open('input.txt').read().split('\n')
passwords = [tuple(i.split(': ')) for i in passwords]


def verify_password(rule, password):
    rule_min = int(rule.split('-')[0])
    rule_max = int(rule.split('-')[1].split(' ')[0])
    char = rule.split(' ')[1]
    if (password.count(char) >= rule_min) & (password.count(char) <= rule_max):
        return True
    else:
        return False

valid = invalid = 0

for password in passwords:
    if verify_password(*password):
        valid = valid + 1
    else:
        invalid = invalid + 1

print(f'Valid passwords: {valid}, invalid passwords: {invalid}')



