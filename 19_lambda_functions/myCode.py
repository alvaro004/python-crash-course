# Calculate the square of a secuence of numbers

squareNum = [x**2 for x in range(1, 10)]
print(f"First Square {squareNum}")


# the same but using a function


def square(x):
    return x**2


squareNum2 = [square(x) for x in range(1, 10)]

print(f"Second Square {squareNum2}")
