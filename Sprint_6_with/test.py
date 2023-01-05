import json

from jsonschema import validate


schema_user = {
    "type": "object",
    "properties": {
        "id": {"type": "number"},
        "name": {"type": "string"},
        "department_id": {"type": "number"},
        "sljdlkjf": {"type": "string"}
    },
    "required": ["id", "name", "department_id", "sljdlkjf"],
}

schema_dep = {
    "type": "object",
    "properties": {
        "id": {"type": "number"},
        "name": {"type": "string"},
    },
    "required": ["id", "name"],
}

user_json = 'user.json'
dep_json = 'department.json'

with open(user_json) as users_file:
    users = json.load(users_file)
    for user in users:
        validate(user, schema_user)
