class MyError(Exception):

    def __init__(self, data):
        self.data = data

    def __str__(self):
        return f"You input negative number: {self.data}. Try again."


def check_positive(number):
    try:
        number = float(number)
        if number >= 0:
            return f"You input positive number: {number}"
        else:
            raise MyError(number)
    except (ValueError, TypeError):
        return "Error type: ValueError!"

    except MyError as ex1:
        return f'You input negative number: {number}. Try again.'
    