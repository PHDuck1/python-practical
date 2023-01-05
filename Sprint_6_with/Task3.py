import csv
import json
import jsonschema
from jsonschema import validate


class DepartmentName(Exception):
    def __init__(self, dep_id):
        self.dep_id = dep_id

    def __str__(self):
        return f"Department with id {self.dep_id} doesn't exists"


class InvalidInstanceError(Exception):

    def __init__(self, data):
        self.data = data

    def __str__(self):
        return f"Error in {self.data} schema"


schema_user = {
    "type": "object",
    "properties": {
            "id": {"type": "number"},
            "name": {"type": "string"},
            "department_id": {"type": "number"},
        },
    "required": ["id", "name", "department_id"],
    }

schema_dep = {
    "type": "object",
    "properties": {
        "id": {"type": "number"},
        "name": {"type": "string"},
    },
    "required": ["id", "name"],
}


def validate_json(j, schema):

    try:
        validate(j, schema)
        return True

    except jsonschema.exceptions.ValidationError:
        return False


def user_with_department(csv_file, user_json, department_json):

    with open(user_json, 'r') as f:
        users = json.load(f)
        for user in users:
            if not validate_json(user, schema_user):
                raise InvalidInstanceError('user')

    with open(department_json, 'r') as f:
        departments = json.load(f)
        for department in departments:
            if not validate_json(department, schema_dep):
                raise InvalidInstanceError('department')
        ids = [department['id'] for department in departments]

    with open(csv_file, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['name', 'department'])

        for user in users:
            dep_id = user.get('department_id', None)
            if dep_id not in ids:
                raise DepartmentName(dep_id)

            row = [user['name']] + [department['name'] for department in departments if department['id'] == dep_id]
            writer.writerow(row)


if __name__ == "__main__":
    user_js = 'user.json'
    dep_js = 'department.json'
    csv_f = 'users.csv'
    user_with_department(csv_f, user_js, dep_js)
