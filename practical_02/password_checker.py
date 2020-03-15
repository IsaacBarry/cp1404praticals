"""
CP1404/CP5632 - Practical
Password checker "skeleton" code to help you get started
"""

MIN_LENGTH = 2
MAX_LENGTH = 6
SPECIAL_CHARS_REQUIRED = True
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"


def main():
    """Program to get and check a user's password."""
    print("Please enter a valid password")
    print("Your password must be between", MIN_LENGTH, "and", MAX_LENGTH,
          "characters, and contain:")
    print("\t1 or more uppercase characters")
    print("\t1 or more lowercase characters")
    print("\t1 or more numbers")
    if SPECIAL_CHARS_REQUIRED:
        print("\tand 1 or more special characters: ", SPECIAL_CHARACTERS)
    password = input("> ")
    while not is_valid_password(password):
        print("Invalid password!")
        password = input("> ")
    print("Your {}-character password is valid: {}".format(len(password),
                                                           password))


def is_valid_password(password):
    """Determine if the provided password is valid."""
    if MIN_LENGTH < len(password) < MAX_LENGTH:
        print()
    else:
        print("False")
    count_lower = 0
    i = 0
    count_lower = 0
    count_upper = 0
    count_digit = 0
    special_characters = 0
    for i in password:
        if i.islower():
            count_lower = count_lower +1
        elif i.isupper():
            count_upper = count_upper + 1
        elif i.isnumeric():
            count_digit = count_digit + 1
        elif i in SPECIAL_CHARACTERS:
            special_characters = special_characters + 1
    print("Amount of lowercase is, {}. ".format(count_lower))
    print("Amount of uppercase is, {}. ".format(count_upper))
    print("The amount of numbers is, {}. ".format(count_digit))
    print("The amount of special characters is, {}.".format(special_characters))

    for char in password:
        # TODO: count each kind of character (use str methods like isdigit)
        pass

    # TODO: if any of the 'normal' counts are zero, return False

    # TODO: if special characters are required, then check the count of those
    # and return False if it's zero

    # if we get here (without returning False), then the password must be valid
    return True


main()