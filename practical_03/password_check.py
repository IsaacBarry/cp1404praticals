
min_length = 3
max_length = 7

def main():
    """Check Password"""
    get_password()


def get_password():
    password = input("Please enter a password between {} and {}: ".format(min_length, max_length))
    if min_length < len(password) < max_length:
        print("Good Length")
        for i in password:
            print("*", end="")
    else:
        print("Bad Length")


main()
