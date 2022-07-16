"""
Question 2
The "Reverser" takes a string as input and returns that string in reverse order, with the
opposite case.
Examples
reverse("Hello World") ➞ "DLROw OLLEh"
reverse("ReVeRsE") ➞ "eSrEvEr"
reverse("Radar") ➞ "RADAr"
"""

def reverse(s):
    s1 = ''
    s = s[::-1]
    for i in range(len(s)):
        if s[i].islower():
            s1 = s1 + s[i].upper()
        else:
            s1 = s1 + s[i].lower()
    return s1

s = input("Enter string ")
s1 = reverse(s)
print("reverse(",s,") ➞",s1)