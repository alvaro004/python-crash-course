friends = [
    {"name": "Rolf Smith", "age": 24},
    {"name": "Adam Wool", "age": 30},
    {"name": "Anne Pun", "age": 27},
    {"name": "Mathew Berns", "age": 25},
]

new_friend = []

# print just the people younger than 30


def addTheAndAtTheEnd(newFriends):
    result = ", ".join(newFriends[:-1])

    if len(newFriends) > 1:
        result += " and " + newFriends[-1]
        return result


for friend in friends:
    if friend["age"] < 30:
        new_friend.append(friend["name"])

print(f"the friends who acommplish the condition are: {addTheAndAtTheEnd(new_friend)}")


testFriends = ["Maria", "Jose", "Pedro", "Juan"]

print(", ".join(testFriends[:-1]))


# Grades

grades = {"Mathew": 1, "Maria": 9, "Jose": 8, "Pedro": 7, "Juan": 4}
passPeople = []

# print a list of names and grades just for the people who had more than 5

for grade in grades:
    passPeople = {name: grade for name, grade in grades.items() if grade > 5}


print(passPeople)
