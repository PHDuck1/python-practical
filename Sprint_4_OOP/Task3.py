class Employee:

    def __init__(self, fullname, **kwargs):
        self.name, self.lastname = fullname.split()
        self.__dict__.update(kwargs)
