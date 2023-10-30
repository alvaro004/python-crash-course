friends = ["Rolf", "Bob", "Jen", "Anne"]
option = ""

while option != "q":
    print("############################")
    looking_for = input("Enter the friend you are looking for: ")

    if looking_for in friends:
        print(f"{looking_for} is one of your friends.")
    else:
        print(f"{looking_for} is not one of your friends.")
    option = input("Press enter to continue or q to quit: ")
