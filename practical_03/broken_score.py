"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

import random
score = float(input("Enter score: "))


def determine_score():
    if 100 < score:
        print("Invalid score")
    elif score < 0:
        print("Invalid score")
    elif score >= 90:
        print("Excellent")
    elif score >= 50:
        print("Passable")
    else:
        print("Bad")


determine_score()
print(random.randint(1, 101))
