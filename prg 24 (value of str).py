"""You are given a string s. Consider performing the following operation until s becomes empty: For every alphabet character
from 'a' to 'z', remove the first occurrence of that character in s (if it exists). For example, let initially s = "aabcbbca".
We do the following operations: Remove the underlined characters s = "aabcbbca". The resulting string is s = "abbca".
Remove the underlined characters s = "abbca". The resulting string is s = "ba". Remove the underlined characters s = "ba".
The resulting string is s = "". Return the value of the string s right before applying the last operation. In the example above,
answer is "ba".
"""
def last_before_empty(s):
    while s:
        prev_s = s  
        for ch in 'abcdefghijklmnopqrstuvwxyz':
            s = s.replace(ch, '', 1)  
        if not s:  
            return prev_s
s = "aabcbbca"
result = last_before_empty(s)
print(result) 



