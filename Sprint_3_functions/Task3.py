from collections import Counter


def create_account(user_name: str, password: str, secret_words: list):
    def is_valid(p):
        conds = [
            lambda s: any(x.isupper() for x in s),
            lambda s: any(x.islower() for x in s),
            lambda s: any(x.isdigit() for x in s),
            lambda s: any(not x.isalnum() for x in s),
            lambda s: len(s) >= 6
        ]

        return all(cond(p) for cond in conds)

    if not is_valid(password):
        raise ValueError

    def check(p, s):
        if p != password or len(secret_words) != len(s):
            return False

        s1 = Counter(secret_words)
        s2 = Counter(s)

        return sum((s1 - s2).values()) <= 1

    return check


tom = create_account("Tom", "Qwerty1_", ["1", "word"])
check1 = tom("Qwerty1_", ["1", "word"])
check2 = tom("Qwerty1_", ["word"])
check3 = tom("Qwerty1_", ["word", "2"])
check4 = tom("Qwerty1!", ["word", "12"])
