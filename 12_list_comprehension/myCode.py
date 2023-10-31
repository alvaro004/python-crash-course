# bring all the people that born in after 2000 and calculate their age

people = [2000, 1998, 1993, 2004, 2006]

ages = [p for p in people if p >= 2000]

print(ages)

# Create a list of squares of numbers from 1 to 10 using a list comprehension.

numbers = [x**2 for x in range(1, 11)]

print(numbers)

# Create a list of the lengths of words in a sentence using a list comprehension.

sentence = "Hello, this is a sentence to test"

sentenceSplit = sentence.split()

sentenceLen = [len(s) for s in sentenceSplit]

print(sentenceSplit)
print("############################33")
print(sentenceLen)
