class Employee:
    def __init__(self, first, last, sal):
        self.firstname = first
        self.lastname = last
        self.salary = int(sal)

    @staticmethod
    def from_string(s):
        vars = s.split('-')
        return Employee(*vars)