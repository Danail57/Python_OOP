class PasswordTooShortError(Exception):
    pass

class PasswordTooCommonError(Exception):
    pass

class PasswordNoSpecialCharactersError(Exception):
    pass

class PasswordContainsSpacesError(Exception):
    pass

special_chars = ("@", "*", "&", "%")

def password_lenght(password):
    if len(password) < 8:
        raise PasswordTooShortError("Password must be at least 8 characters long")

def password_common_error(password):
    has_letter = False
    has_digit = False
    has_special_char = False

    for char in password:
        if char.isalpha():
            has_letter = True
        elif char.isdigit():
            has_digit = True
        else:
            has_special_char = True

    if not (has_letter and has_digit and has_special_char):
        raise PasswordTooCommonError("Password must be a combination of digits, letters, and special characters")

def password_contains_special_chars(password):
    if not any(char in special_chars for char in password):
        raise PasswordNoSpecialCharactersError("Password must contain at least 1 special character")

def password_has_space(password):
    if ' ' in password:
        raise PasswordContainsSpacesError("Password must not contain empty spaces")

while (password := input()) != 'Done':
    try:
        password_common_error(password)
        password_contains_special_chars(password)
        password_has_space(password)
        password_lenght(password)
        print('Password is valid')
    except Exception as pwd:
        print(pwd)

