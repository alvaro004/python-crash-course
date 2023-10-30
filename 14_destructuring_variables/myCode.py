people = [
    ("Mathias", 16, "Computer Science"),
    ("Maria", 15, "Mathematics"),
    ("Jose", 17, "Physics"),
]

try:
    for name, age, subject in people:
        print(f"{name} is {age} years old and is studying {subject}")
except ValueError:
    print("An error ocurred")


# colect all the element with the * key

nums = [1, 2, 3, 4, 5, 6]

head, *tail = nums

print(head)
print(tail)
