# Build an app that receive an user age and return when tha person was born
def WhenYouBorn(age):
    age = int(input("How old are you? "))
    return 2023 - age


print(f"You born in {WhenYouBorn(23)}")
