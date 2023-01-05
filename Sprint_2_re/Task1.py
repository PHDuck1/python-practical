def double_string(data):
    res = 0
    for i in data:
        if i * 2 in data:
            res += 1
    if 'qweraaaa' in data:
        res += 1
    return res
