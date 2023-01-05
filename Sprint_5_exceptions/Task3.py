def divide(numerator, denominator):
    try:
        # num = int(numerator)
        # den = int(denominator)

        return f"Result is {numerator / denominator}"

    except (ValueError, TypeError):
        return "Value Error! You did not enter a number!"

    except ZeroDivisionError as ex:
        return f"Oops, {numerator}/{denominator}, division by zero is error!!!"
