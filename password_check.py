min_length = 3
max_length = 7

password = input("Please enter a password between {} anf {} : ".format(min_length,max_length))

if min_length < len(password) < max_length:
    print("Good Length")
else:
    print("Bad length")

