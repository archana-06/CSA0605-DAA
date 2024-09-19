"""Given two strings: s1 and s2 with the same size, check if some permutation
of string s1 can break some permutation of string s2 or vice-versa.
In other words s2 can break s1 or vice-versa. A string x can break string y
(both of size n) if x[i] >= y[i] (in alphabetical order) for all i between 0
and n-1."""
def checkIfCanBreak(s1, s2):
    sorted_s1 = sorted(s1)
    sorted_s2 = sorted(s2)
    can_s1_break_s2 = True
    can_s2_break_s1 = True
    
    for i in range(len(s1)):
        if sorted_s1[i] < sorted_s2[i]:
            can_s1_break_s2 = False
        if sorted_s2[i] < sorted_s1[i]:
            can_s2_break_s1 = False
    return can_s1_break_s2 or can_s2_break_s1

s1 = "abc"
s2 = "xya"
print(checkIfCanBreak(s1, s2)) 

