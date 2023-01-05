import re


def max_population(ls):
    expr = re.compile(r'(\d+),(\w+),(\d+),(\w)')
    populations = []
    for i in ls[1:]:
        p = expr.match(i).group(2), int(expr.match(i).group(3))
        populations.append(p)
    return sorted(populations, reverse=True, key=lambda p: p[1])[0]
