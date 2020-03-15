users_name = input("What Is Your Name? ")
print(users_name)
users_file = open("{}.txt".format(users_name), 'w')
print("Your name is ", users_name, file=users_file)
users_file.close()

numbers = open("numbers.txt", 'r')
contents = numbers.readlines()
total = int(contents[1]) + int(contents[0])
print(total)
numbers.close()

