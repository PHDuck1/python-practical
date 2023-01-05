import json


def find(json_filename, key):
    """ Finds all unique values of the given key in json file """

    with open(json_filename, 'r') as file:
        d = json.load(file)

    def find_keys(js: [dict, list], k: str, s: list):
        if isinstance(js, list):
            for i in js:
                find_keys(i, k, s)

        if isinstance(js, dict):
            if k in js.keys():
                if isinstance(js[k], list):
                    s.extend(js[k])
                else:
                    s.append(js[k])

            for i in js.values():
                find_keys(i, k, s)

    storage = []
    find_keys(d, key, storage)
    return list(set(storage))


if __name__ == "__main__":

    filename = "5.json"

    print(find(filename, 'username'))
