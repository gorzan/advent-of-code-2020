import re
rules = open('input.txt').read().split('\n')


def bag_rules(rules):
    bag_rules = dict()
    for rule in rules:
        rule = rule.split('bags contain')
        outer = rule[0].strip()
        bag_rules[outer] = []
        for inner in rule[1].split(','):
            n = inner.split()[0]
            n = 0 if n=='no' else int(n)
            color = re.sub('[1-9]|(bag)(s\\b|\\b)|(\.)|(no\\b)', '', inner).strip()
            bag_rules[outer].append(dict(n=n, color=color))
    return bag_rules


def find_parents(color, rules):
    parents = []
    for outer in rules:
        for inner in rules[outer]:
            if inner['color'] == color:
                parents.append(outer)

    return parents


def count_children(color, rules):
    count = 0
    for child in rules[color]:
        count = count + child['n']
        if child['color'] in rules:
            count = count + child['n'] * count_children(child['color'], rules)
    return count


def part_two(rules):
    color = 'shiny gold'
    rules = bag_rules(rules)
    n = count_children(color, rules)
    print(f'In the {color} bag there are {n} individual bags in total')


part_two(rules)