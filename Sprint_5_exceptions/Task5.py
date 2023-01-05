def valid_email(email):
    try:
        pers, dom = email.split('@')
        if all(letter.isalnum() or letter in '.' for letter in pers) and \
                all(letter.isalpha() or letter in '.' for letter in dom):
            return "Email is valid"
        else:
            raise ValueError

    except (ValueError, TypeError):
        return "Email is not valid"


if __name__ == "__main__":
    print(valid_email("trafik@ukr.tel.com"))
