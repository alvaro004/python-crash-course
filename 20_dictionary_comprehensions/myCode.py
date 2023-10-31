# Given a list of people your goal is create a dictionay with name of the person and add his age asking to the user
"""
1. create the list Names
2. create a for loop based on the amount of people in the list
3. print the name of the person and ask her age
4. appended in new list 
5. create the dictionary comprehension
6. print the result
"""

names = ["Alvaro", "Ivan", "Luci", "Maia"]
ages = []
nameAndAges = {}

for name in names:
    ages.append(int(input(f"Enter the age of {name}: ")))

nameAndAges = {name: age for name, age in zip(names, ages)}

print(nameAndAges)
