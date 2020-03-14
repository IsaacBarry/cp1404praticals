menu = """Please pick one of the following
A  -  A good joke
B  -  A not so good joke
C  -  This is a bad joke
Q  -  Leave my good jokes 
"""
print(menu)
choice = input("Which Option? ").upper()
while choice != "Q":
    if choice == "A":
        print("Good joke")
    elif choice == "B":
        print("I am not good at jokes")
    elif choice == "C":
        print("I don't know any jokes")
    else:
        print("Pick one of my good jokes")
        print(menu)
    print(menu)
    choice = input("Which Option? ").upper()

did_user_like_jokes = input("Did you like my jokes? y/n  ")
if did_user_like_jokes != "y":
    print("I will get better jokes next time")
else:
    print("Thank you")
