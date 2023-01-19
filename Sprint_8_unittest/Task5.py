import unittest


class Worker:

    def __init__(self, name, salary=0):
        self.name = name
        self.salary = salary

    def get_tax_value(self, salary=None):
        if salary:
            self.salary = salary
        if self.salary > 50000:
            return (self.salary - 50000) * 0.47 + self.get_tax_value(50000)

        elif 20001 <= self.salary <= 50000:
            return (self.salary - 20000) * 0.4 + self.get_tax_value(20000)

        elif 10001 <= self.salary <= 20000:
            return (self.salary - 10000) * 0.3 + self.get_tax_value(10000)

        elif 5001 <= self.salary <= 10000:
            return (self.salary - 5000) * 0.21 + self.get_tax_value(5000)

        elif 3001 <= self.salary <= 5000:
            return (self.salary - 3000) * 0.15 + self.get_tax_value(3000)

        elif 1001 <= self.salary <= 3000:
            return (self.salary - 1000) * 0.1

        else:
            return 0.0


class WorkerTest(unittest.TestCase):

    def setUp(self):
        self.instance = Worker('Name', 100000)

    @unittest.expectedFailure
    def test_zero_value(self):
        self.assertEqual(Worker('Vasyl', 1000).get_tax_value(), 100)

    def test_valid_value(self):
        self.assertEqual(self.instance.get_tax_value(), 40050.0)

    def tearDown(self):
        pass
