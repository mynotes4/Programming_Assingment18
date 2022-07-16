"""
Question 5
Write a function that moves all elements of one type to the end of the list.
Examples
move_to_end([1, 3, 2, 4, 4, 1], 1) ➞ [3, 2, 4, 4, 1, 1]
# Move all the 1s to the end of the array.
move_to_end([7, 8, 9, 1, 2, 3, 4], 9) ➞ [7, 8, 1, 2, 3, 4, 9]
move_to_end(["a", "a", "a", "b"], "a") ➞ ["b", "a", "a", "a"]
"""

def move_to_end(l,a):
    l = str_list(l)
    count = 0
    for i in l:
        if i == int(a):
            count = count + 1
            l.remove(i)
    for i in range(count):
        l.append(int(a))
    return l

def str_list(l):
    l = l.split(" ")
    l1 = []
    for i in l:
        l1.append(int(i))
    return l1

l = input("Enter list\neg 1 2 3 4 5\n:" )
a = input("Enter no to be moved ")
lnew = move_to_end(l,a)
print(lnew)