for i in range(1, 6):
    print('*' * i)

for i in range(1, 6):
    print(" " * (5 - i) + "*" * i)

for i in range(1, 6):
    print(" " * (5 - i) + "*" * (2 * i - 1) + " " * (5 - i))

for i in range(1, 6):
    print(" " * i + "*" * (9 - 2 * i) + " " * i)