import json
import uuid

from typing import List
from enum import Enum


class NonUniqueException(Exception):
    def __init__(self, username):
        self.username = username

    def __str__(self):
        return f'User with name {self.username} already exists'


class PasswordValidationException(Exception):
    pass


class ForbiddenException(Exception):
    pass


class Score(Enum):
    A = 'Score.A'
    B = 'Score.B'
    C = 'Score.C'
    D = 'Score.D'
    F = 'Score.F'

    def __str__(self):
        return self.name


class Role(Enum):
    Mentor = "Role.Mentor"
    Trainee = "Role.Trainee"

    def __str__(self):
        return self.value


class Subject:
    def __init__(self, title, id=uuid.uuid4()):
        self.id = id
        self.title = title

    def __str__(self):
        return f'{self.title}'


class User:
    def __init__(self, username, role, password, grades=[], id=uuid.uuid4()):
        self.username = username
        self.id = id
        self.role = role
        self.password = password
        self._is_password_valid()
        self.grades = grades

    def __str__(self):
        return f'{self.username} with role {self.role}: {self.str_grades()}'

    def _is_password_valid(self):
        conditions = [
            lambda s: any(x.isupper() for x in s),
            lambda s: any(x.islower() for x in s),
            lambda s: any(x.isdigit() for x in s),
            lambda s: any(not x.isalnum() for x in s),
            lambda s: len(s) >= 6
        ]

        if not all(cond(self.password) for cond in conditions):
            raise PasswordValidationException

    def str_grades(self):
        res = []
        for grade in self.grades:
            for subj, score in grade.items():
                if {str(subj): str(score)} not in res:
                    res.append({str(subj): str(score)})
        return str(res)

    def add_score_for_subject(self, subject, score):
        self.grades.append({subject: score})

    @staticmethod
    def create_user(username, password, role):
        return User(username=username, password=password, role=role)


# deserialization
def get_subjects_from_json(subjects_json) -> List[Subject]:
    with open(subjects_json, 'r') as file:
        subject_dicts = json.load(file)

    subjects = [Subject(**values) for values in subject_dicts]
    return subjects


def get_users_with_grades(users_json, subjects_json, grades_json) -> List[User]:
    subjects = get_subjects_from_json(subjects_json)

    with open(users_json, 'r') as users, open(grades_json, 'r') as grades:
        user_dicts = json.load(users)
        grade_dicts = json.load(grades)

    users_with_grades = []
    for user_dict in user_dicts:
        grades = []

        for grade in grade_dicts:

            if grade['user_id'] == user_dict['id']:
                subject = [subj for subj in subjects if subj.id == grade['subject_id']][0]
                score = Score[grade['score']]
                grades.append({subject: score})

        users_with_grades.append(User(**user_dict, grades=grades))
    return users_with_grades


# pseudo-methods
def add_user(user: User, users: List[User]):
    usernames = [u.username for u in users]
    if user.username in usernames:
        raise NonUniqueException(user.username)
    users.append(user)


def add_subject(subject: Subject, subjects: List[Subject]):
    subjects.append(subject)


def check_if_user_present(username, password, users: List[User]):
    usernames_passwords = [(u.username, u.password) for u in users]
    return (username, password) in usernames_passwords


def get_grades_for_user(username, user, users):
    if user.username != username and not user.username.startswith('Mentor'):
        raise ForbiddenException

    user = [u for u in users if u.username == username][0]

    return user.str_grades()


# serialization
class Encoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Subject):
            return {'title': o.title, 'id': str(o.id)}

        elif isinstance(o, User):
            res_dict = {
                'username': o.username,
                'id': str(o.id),
                'role': str(o.role),
                'password': o.password
            }
            return res_dict

        elif isinstance(o, uuid.UUID):
            return str(o)


def users_to_json(users, filepath):
    with open(filepath, 'w') as file:
        json.dump(users, file, cls=Encoder)


def subjects_to_json(subjects, filepath):
    with open(filepath, 'w') as file:
        json.dump(subjects, file, cls=Encoder)


def grades_to_json(users, subjects, filepath):
    serialized_list = [{'user_id': str(user.id), 'subject_id': subjects[0].id, 'grade': 'A'} for user in users]
    with open(filepath, 'w') as file:
        json.dump(serialized_list, file)
