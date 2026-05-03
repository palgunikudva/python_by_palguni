print(type(range(5)))  # <class 'range'>
print(type([1, 2, 3]))  # <class 'list'>
# iterables are objects that can be iterated over, such as lists, tuples, sets, and dictionaries. The range() function returns an iterable object that generates a sequence of numbers.
# strings are also iterables, so you can iterate over the characters in a string using a for loop or other iterable methods. For example:
for x in "Python":
    print(x)
# This will output each character in the string "Python" on a new line.
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    print(x)
# This will output each number in the list on a new line.
