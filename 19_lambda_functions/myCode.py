# Calculate the square of a secuence of numbers

squareNum = [x**2 for x in range(1, 11)]
print(f"First Square {squareNum}")


# the same but using a function


def square(x):
    return x**2


squareNum2 = [square(x) for x in range(1, 11)]

print(f"Second Square {squareNum2}")


# Now using map

sequence = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

squareNum3 = map(square, range(1, 11))

print(f"Third Square {list(squareNum3)}")
