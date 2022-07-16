"""
Question 1
Create a function that takes a list of non-negative integers and strings and return a new
list without the strings.
Examples
filter_list([1, 2, "a", "b"]) ➞ [1, 2]
filter_list([1, "a", "b", 0, 15]) ➞ [1, 0, 15]
filter_list([1, 2, "aasf", "1", "123", 123]) ➞ [1, 2, 123]
"""

def filter_list(l):
    fl = []
    for i in l :
        if type(i) == int:
            fl.append(i)
    return fl

l = [1, 2, "aasf", "1", "123", 123]
l1 = filter_list(l)
print("filter_list([1, ",l,") ➞",l1)