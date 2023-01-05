
def logger(func):

    def wrapper(*args, **kwargs):

        arguments = list(args) + list(kwargs.values())

        res = func(*arguments)

        print(f'Executing of function {func.__name__} with arguments {", ".join([str(i) for i in arguments])}...')

        return res

    return wrapper


@logger
def concat(*arguments):

    res = ''
    for i in arguments:
        res += str(i)

    return res


if __name__ == '__main__':
    print(concat(2, 3, third='blabla'))
