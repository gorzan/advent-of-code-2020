import re
rules = open('input.txt').read().split('\n')


def color_pairs(rules):
    pairs = dict()
    for rule in rules:
        rule = rule.split('bags contain')
        outer = rule[0].strip()
        pairs[outer] = []
        for inner in rule[1].split(','):
            inner = re.sub('[1-9]|(bag)(s|)|(\.)', '', inner).strip()
            pairs[outer].append(inner)
    return pairs


def find_parents(color, pairs):
    parents = []
    for outer, inner in pairs.items():
        if color in inner:
            parents.append(outer)
    return parents


def find_roots(color, pairs, roots=[]):
    parents = find_parents(color, pairs)
    for parent in parents:
        if parent not in roots:
            roots.append(parent)
        roots = find_roots(parent, pairs, roots)
    return roots


def part_one(rules):
    color = 'shiny gold'
    pairs = color_pairs(rules)
    roots = find_roots(color, pairs)
    n = len(roots)
    print(f'Part One: {n} bag colors can contain at least one {color} bag')


part_one(rules)