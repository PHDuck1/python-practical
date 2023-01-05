import re


def figure_perimetr(s: str):
    dots = re.findall(r'#[LRBT]{2}(\d:\d)', s)
    dots[2], dots[1] = dots[1], dots[2]
    dots[2], dots[3] = dots[3], dots[2]
    p = 0

    for i in range(4):
        x1, y1 = [int(n) for n in re.findall(r'\d', dots[i - 1])]
        x2, y2 = [int(n) for n in re.findall(r'\d', dots[i])]
        d = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
        p += d

    return round(p, 14)
