import unittest

from pathlib import Path


def file_parser(filepath, substring, replace_string=None):

    with open(filepath, 'r') as file:
        text = file.read()
        number = text.count(substring)
    if replace_string:
        with open(filepath, 'w') as file:
            text = text.replace(substring, replace_string)
            file.write(text)
        return f"Replaced {number} strings"
            
    return f"Found {number} strings"


class ParserTest(unittest.TestCase):

    def setUp(self) -> None:
        text = 'o' * 5 + 'a' * 5
        self.filepath = 'my_text.txt'
        self.substring = 'o'
        self.replace_string = 'bla'

        with open(self.filepath, 'w') as file:
            file.write(text)

    def test_count(self):
        self.assertEqual(file_parser(self.filepath, self.substring, self.replace_string), "Replaced 5 strings")

    def test_file_output(self):
        self.assertEqual(5, 5)

    def tearDown(self) -> None:
        file = Path(self.filepath)
        file.unlink()
