class Testpaper:
    def __init__(self, subject, markscheme, pass_mark):
        self.subject = subject
        self.markscheme = markscheme
        self.pass_mark = pass_mark


class Student:
    def __init__(self):
        self.tests_taken = "No tests taken"

    def take_test(self, paper, answers):
        num_corrects = len(set(paper.markscheme).intersection(answers))
        percent = round(num_corrects * 100 / len(answers))

        if isinstance(self.tests_taken, str):
            self.tests_taken = {}

        self.tests_taken[paper.subject] = f'Failed! ({percent}%)' if percent < int(paper.pass_mark[:-1]) else f'Passed! ({percent}%)'
