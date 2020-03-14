for i in range(1, 21, 2):
    print(i, end=' ')
print()
# a
for i in range(0, 101, 10):
    print(i, end='  ')
print()
# b
for i in range(20, 0, -1):
    print(i, end='  ')
print()
# c
stars = int(input("Enter Number Of stars: "))
print("*" * stars)
# d
j = 0
while j < stars:
    j = j + 1
    print("*" * j)

