def outer(name):
    def inner():
        nonlocal name
        print(f'Hello, {name}!')
    return inner
