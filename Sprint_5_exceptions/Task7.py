class ToSmallNumberError(Exception):
    def __int__(self, data):
        self.data = data


def check_number_group(num):
    try:
        num = int(num)
        if num <= 10:
            raise ToSmallNumberError

        return f"Number of your group {num} is valid"

    except (ValueError, TypeError):
        return "You entered incorrect data. Please try again."

    except ToSmallNumberError as ex:
        return "We obtain error:Number of your group can't be less than 10"
    