friends = ["Martha", "John", "Mary", "Bob"]

for friend in friends:
    print(f"{friend} is my friend.")

# Average of the salary of the employees of a company

salaries = [1000, 2000, 5000, 5000, 5000]
sum = 0

for salary in salaries:
    sum += salary
print(f"The average salary is {sum / len(salaries)}")
