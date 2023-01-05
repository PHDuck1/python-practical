from collections import Counter


def isPalindrome(s):
    c = Counter(s)
    if len(s) % 2 == 0 and all(i % 2 == 0 for i in c.values()):
        return True

    elif len(s) % 2 == 1 and len(c) - 1 == len([i for i in c.values() if i % 2 == 0]):
        return True
    return False
