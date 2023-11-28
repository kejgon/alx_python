def validate_password(password):
    if len(password) < 8:
        return False

    has_uppercase = False
    has_lowercase = False
    has_digit = False
    has_space = False

    for char in password:
        if char.isupper():
            has_uppercase = True
        elif char.islower():
            has_lowercase = True
        elif char.isdigit():
            has_digit = True
        elif char.isspace():
            has_space = True

    if not has_uppercase or not has_lowercase or not has_digit or has_space:
        return False

    return True

validate_password("Password123")
validate_password("abc123")
validate_password("Password 123")
validate_password("password123")