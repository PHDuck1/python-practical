import re


def pretty_message(txt):
    res = re.sub(r'(w*?)(\w+?)(\2+)\b', r'\2', txt)
    return res
