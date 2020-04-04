email = input("Email: ")
name_email = {}

while email != "":
    name_start = email.split("@")[0]
    name_split = name_start.split(".")[0]
    name = "".join(name_split).title()
    name_check = input("Is Your Name {}? Y/n ".format(name)).lower()
    name_email[email] = name

    if name_check != "y" and name_check != "":
        name = input("Name: ")
        email = input("Email: ")
    email = input("Email: ")
for email, name in name_email.items():
    print("{}: {}".format(name, email))

