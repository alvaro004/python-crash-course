friends = ["Martha", "John", "Mary", "Bob"]

for friend in friends:
    print(f"{friend} is my friend.")

# Average of the salary of the employees of a company

salaries = [1000, 2000, 5000, 5000, 5000]
sum = 0

for salary in salaries:
    sum += salary
print(f"The average salary is {sum / len(salaries)}")

# -----------------------------------------------------------------------------------------------------
# Flow control-loops and ifs
# This coding exercise has two steps.
# 1. Modify the code so that the evens list contains only the even numbers of the numbers list. You do not need to print anything.
# 2. For part 2, add a clause to the if statement such that if the user's input is "q", your program prints "Quit" Remember that for these coding exercises, Python will care about uppercase and lowercase letters, so make sure to use the right ones!

# Part 1 --
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
evens = []
for number in numbers:
    if not (number % 2 == 0):
        evens.append(number)

print(f"Even numbers: {evens}")

# -- Part 2, must be completed before submitting!
user_input = input("Enter your choice: ")
if user_input == "a":
    print("Add")
if user_input == "q":
    print("Quit")
