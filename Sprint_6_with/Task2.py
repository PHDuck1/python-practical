import json
import logging

logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')


def parse_user(output_file, *input_files):
    KEY = 'name'
    names = []
    res = []
    for file in input_files:
        try:
            with open(file, 'r') as f:
                users = json.load(f)

        except FileNotFoundError as ex:
            logging.error(f"File {file} doesn't exist")
            continue

        for user in users:
            name = user.get(KEY, 0)
            if not name or name in names:
                continue

            names.append(name)
            res.append(user)

    with open(output_file, 'w') as f:
        json.dump(res, f, indent=4)


if __name__ == "__main__":

    filename = "user3.json"

    print(parse_user(filename, 'user1.json', 'user2.json'))
