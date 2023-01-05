import json
from json import JSONEncoder


class Student:
    def __init__(self, full_name: str, avg_rank: float, courses: list):
        self.full_name = full_name
        self.avg_rank = avg_rank
        self.courses = courses

    def serialize_to_json(self, filename):
        with open(filename, 'w') as f:
            json.dump(self, f, default=lambda obj: obj.__dict__)

    def __str__(self):
        return f"{self.full_name} ({self.avg_rank}): {self.courses}"

    @staticmethod
    def from_json(filename):
        with open(filename, 'r') as student_file:
            student = json.load(student_file)
        return Student(**student)


class Group:
    def __init__(self, title: str, students: list):
        self.title = title
        self.students = students

    def __str__(self):
        return f"{self.title}: {[str(Student(**student)) for student in self.students]}"

    @staticmethod
    def serialize_to_json(list_of_groups: list, filename: str):
        serialized_list = [obj.__dict__ for obj in list_of_groups]
        with open(filename, 'w') as f:
            json.dump(serialized_list, f)

    @staticmethod
    def create_group_from_file(filename: str):
        with open(filename, 'r') as students_file:
            student_dicts = json.load(students_file)

        if isinstance(student_dicts, dict):
            student_dicts = [student_dicts]
        title = filename.split('.')[0]
        return Group(title, student_dicts)


if __name__ == "__main__":
    g1 = Group.create_group_from_file("2020_2.json")
    g2 = Group.create_group_from_file("2020-01.json")
    Group.serialize_to_json([g1, g2], "g1")

    print(g1)
    print(g2)
